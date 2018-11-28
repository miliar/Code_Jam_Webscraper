#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

//#define DEBUG

void read_blocks(int nblocks, vector<int>& res)
{
    for(int j=0; j<nblocks;++j)
    {
        string tmp;
        cin >> tmp;
        int value = 0;
        for(int i=2; i<tmp.size();++i)
        {
            value = value*10 + (tmp[i] - '0');
        }
        int k = 5-tmp.size()+2;
        for(int i=0; i<k;++i)
        {
            value *= 10;
        }
        res.push_back(value);
    }
    std::sort(res.begin(), res.end());
}

void calc_dummy(vector<int>& blocks_ken, vector<int>& dummy_blocks, const vector<int>& blocks_naomi)
{
    dummy_blocks.clear();
    for(int i=0; i<blocks_ken.size()-1;++i)
    {
        int value = blocks_ken[i+1] - blocks_ken[i] - 1;
        dummy_blocks.push_back(value);
    }
    int value = 99999 - blocks_ken[blocks_ken.size()-1];
    dummy_blocks.push_back(value);

    for(int i=blocks_naomi.size()-1; i>=0 ;--i)
    {
        for(int j=blocks_ken.size()-1; j>=0; --j)
        {
            if (blocks_naomi[i] > blocks_ken[j])
            {
                --dummy_blocks[j];
                break;
            }
        }
    }

}

void print_vector(const vector<int>& vec)
{
    for(int i=0; i<vec.size();++i)
    {
        cout << vec[i] << " " ;
    }

    cout << endl;
}

int ken_index(int chosen_naomi, vector<int>& blocks_ken, int& ken_weight)
{
    if (blocks_ken.empty())
    {
        return -1;
    }
    for(int i=0; i<blocks_ken.size(); i++)
    {
        if (blocks_ken[i] > chosen_naomi)
        {
            ken_weight = blocks_ken[i];
            return i;
        }
    }

    ken_weight = blocks_ken[0];
    return 0;
}


int warScore(const vector<int>& blocks_naomi_, const vector<int>& blocks_ken_)
{
    vector<int> blocks_ken = blocks_ken_;
    vector<int> blocks_naomi = blocks_naomi_;
    int nround = blocks_naomi.size();

    int score = 0;

    for(int i=0; i<nround;++i)
    {
        int ken_weight;
        int naomi_weight = blocks_naomi.front();
        int ki = ken_index(naomi_weight, blocks_ken, ken_weight);

        blocks_naomi.erase(blocks_naomi.begin());
        blocks_ken.erase(blocks_ken.begin()+ki);

        if (naomi_weight > ken_weight)
        {
            ++score;
        }
    }
    return score;
}

int dWarScore(const vector<int>& blocks_naomi_, const vector<int>& blocks_ken_,
             const vector<int>& dummy_blocks_)
{
    vector<int> blocks_ken = blocks_ken_;
    vector<int> blocks_naomi = blocks_naomi_;
    vector<int> dummy_blocks = dummy_blocks_;
    int nround = blocks_naomi.size();
    int score = 0;

    for(int i=0; i<nround;++i)
    {
#ifdef DEBUG 
        cout << "Round # " << i+1 << endl;
        cout << "Before playing:" << endl;
        print_vector(blocks_naomi);
        print_vector(blocks_ken);
        print_vector(dummy_blocks);
#endif
        int ken_weight;
        int naomi_weight = blocks_naomi.front();
        int told_naomi = naomi_weight;
        int ki = -0;
        if (blocks_ken.size() == 1)
        {
            //let it go
            ki = 0;
            ken_weight = blocks_ken.front();

            if (naomi_weight > ken_weight)
            {
                ++score;
            }
            break;
        }

        if (naomi_weight > blocks_ken.back())
        {
            //all win
            score += (nround-i);
            return score;
        }

        if (naomi_weight < blocks_ken.front())
        {
            //force ken use the max
            //told_naomi will be in cetween max and second max of kens
            ki = blocks_ken.size()-2;
        }
        else
        {
            ki = blocks_ken.size()-1;
            //force ken use the smallest, which means cheat him with a number > max of kens
        }

        bool cheated = false;
        while(ki>=0)
        {
            if (dummy_blocks[ki] > 0)
            {
                told_naomi = blocks_ken[ki]+1;
                --dummy_blocks[ki];
                cheated = true;
                break;
            }
            else
            {
                --ki;
            }
        }

        if (ki < 0)
        {
            ki = 0;
        }

        if (cheated)
        {
#ifdef DEBUG
            cout << "we can cheat ken with " << told_naomi << endl;
#endif
            ki = ken_index(told_naomi, blocks_ken, ken_weight);
        }
        else
        {
#ifdef DEBUG
            cout << "we can't cheat in this interval" << endl;
#endif
            ki = ken_index(naomi_weight, blocks_ken, ken_weight);
        }

        blocks_ken.erase(blocks_ken.begin() + ki );
        if (ki>0)
        {
            dummy_blocks[ki-1] += dummy_blocks[ki];
        }
        dummy_blocks.erase(dummy_blocks.begin() + ki);


        blocks_naomi.erase(blocks_naomi.begin());

#ifdef DEBUG
        cout << "Naomi chooses " << naomi_weight << endl;
        cout << "Naomi tells " << told_naomi << endl;
        cout << "Ken chooses " << ken_weight << endl;
#endif

        if (naomi_weight > ken_weight)
        {
#ifdef DEBUG
            cout << "naomi win" << endl;
#endif
            ++score;
        }
#ifdef DEBUG
        else
        {
            cout << "naomi lose" << endl;
        }
#endif
#ifdef DEBUG 
        cout << "Round # " << i+1 << endl;
        cout << "After playing:" << endl;
        print_vector(blocks_naomi);
        print_vector(blocks_ken);
        print_vector(dummy_blocks);
#endif
    }

    return score;
}

int main()
{

    int T;
    cin >> T;
    for(int icase=0; icase<T; ++icase)
    {
        int dwar = 0;
        int war = 0;
        
        vector<int> blocks_naomi;
        vector<int> blocks_ken;
        vector<int> dummy_blocks;

        int nblocks;
        cin >> nblocks;

        read_blocks(nblocks, blocks_naomi);
        read_blocks(nblocks, blocks_ken);
        calc_dummy(blocks_ken, dummy_blocks, blocks_naomi);

        war = warScore(blocks_naomi, blocks_ken);
        dwar = dWarScore(blocks_naomi, blocks_ken, dummy_blocks);



        cout << "Case #" << icase+1 << ": " << dwar << " " << war << endl;
    }
}

