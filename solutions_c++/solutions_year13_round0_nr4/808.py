
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <map>

using namespace std;

int getline_int(istream& ist)
{
    string line;
    getline(ist,line);
    istringstream ss(line.c_str());

    int res = 0;
    ss >> res;
    return res;
}

int get_int(istream& ist)
{
    int res = 0;
    ist >> res;
    return res;
}

string getln_string(istream& ist)
{
    string line;
    getline(ist,line);
    return line;
}

struct chest
{
    int opener;
    multiset<int> keyset;
    bool empty;
};

template<class T>
void report(const string& h, T& p)
{
    cout << h;
    for (auto i = p.begin(); i != p.end(); ++i)
    {
        cout << " " << *i;
    }
    cout << endl;
}

class Solver
{
public:
    Solver(size_t nk, size_t nc) : _nchests(nc),_nkeys(nk),_starters(),_chests(),_nonnavig()
    {

        for (int i = 0; i <= _nchests; ++i)
        {
            chest c;
            c.keyset.clear();
            c.opener = 0;
            _chests.push_back(c);
        }
    }

    void add(size_t ic, size_t key)
    {
        _chests[ic].keyset.insert(key);
    }

    void set_opener(size_t ic, size_t key)
    {
        _chests[ic].opener = key; 
    }

    void add_starter(int s)
    {
        _starters.insert(s);
    }

    bool walk(vector<int>& path,set<int>& untrodden,multiset<int>& posessed)
    {
        //exclude known bad sets
        if (_nonnavig.find(untrodden) != _nonnavig.end())
        {
            return false;
        }

        //exclude sets that have incorrect key supply-demand balance
        {
            multiset<int> pool = posessed;
    
            for (auto x = untrodden.begin(); x != untrodden.end(); ++x)
            {
                chest& c = _chests[*x];
                pool.insert(c.keyset.begin(),c.keyset.end());
            }
            for (auto x = untrodden.begin(); x != untrodden.end(); ++x)
            {
                chest& c = _chests[*x];
                auto k = pool.find(c.opener);
                if (k == pool.end())
                {
                    return false;
                }
                else
                {
                    pool.erase(k);
                }
            }
        }

        static int kk = 0;
        set<int> u = untrodden;
        for (auto i = untrodden.begin(); i != untrodden.end(); ++i)
        {
            chest& c = _chests[*i];
            int step = *i;
            auto ineeded_key = posessed.find(c.opener);
            if (ineeded_key != posessed.end())
            {
//                cout << "STEP=" << step << endl;
                path.push_back(step);
                u.erase(step);
                posessed.erase(ineeded_key);
                posessed.insert(c.keyset.begin(),c.keyset.end());
                if (u.empty())
                {
                    return true;
                }
                else
                { 
                    bool result = walk(path,u,posessed);
                    if (result)
                    {
                        return true;
                    }
                    else
                    {
                        for (auto j = c.keyset.begin(); j != c.keyset.end(); ++j)
                        {
                            posessed.erase(posessed.find(*j));
                        }
                        posessed.insert(c.opener);
                        u.insert(step);
//                        cout << "S=" << path.back() << " s = " << step << endl;
                        path.pop_back();
                    }
                }
            }
        }
        _nonnavig.insert(untrodden);
        return false;
    }


    string result()
    {
        vector<int> path;
        set<int> untrodden;
        multiset<int> possessed(_starters);
        for (int i = 1; i <= _nchests; ++i)
        {
            untrodden.insert(i);
        }
        if (walk(path,untrodden,possessed))
        {
            ostringstream res;
            for (auto p = path.begin(); p != path.end(); ++p)
            {
                res << *p << ' ';
            }
            return res.str();
        }
        else
        {    
            return "IMPOSSIBLE";
        }
    }
    void disp()
    {
        for (auto ic = _chests.begin()+1; ic != _chests.end();++ic)
        {
            chest& c = *ic;
            report(" chest : ", c.keyset);
            cout << c.opener << endl << endl;
        }
    }
private:
    size_t  _nchests;
    size_t  _nkeys;
    multiset<int> _starters;
    vector<chest> _chests;
    set<set<int> > _nonnavig;
};


void show(int c, const char* outcome)
{
    cout << "Case #" << (c+1) << ": " << outcome << endl;
}

int main (int argc, char *argv[])
{
    int cases = getline_int(cin);
    for (int c = 0; c < cases; ++c)
    {
        int nkeys = 0;
        cin >> nkeys;
        int nchests = 0;
        cin >> nchests;
        getln_string(cin);


        Solver s(nkeys,nchests);

        for (int i = 0; i < nkeys; ++i)
        {
            int ktype = get_int(cin);
            s.add_starter(ktype);
        }
        getln_string(cin);

        for (int i = 1; i <= nchests; ++i)
        {
            int ktype = get_int(cin);
            s.set_opener(i,ktype);

            int nkeys = get_int(cin);
            for (int ik = 0; ik < nkeys; ++ik)
            {
                int k = get_int(cin);
                s.add(i,k);
            }
            getln_string(cin);
        }
        //s.disp();
        show(c,s.result().c_str());
    }
    return 0;
}

