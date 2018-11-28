#include<iostream>
#include<cmath>
#include<ios>
#include<vector>
#include<algorithm>
#include<fstream>

using namespace std;
typedef long long ll;
typedef long double ld;

int main(){
    ios_base::sync_with_stdio(0);
    ifstream in;
    ofstream ou;
    ou.open("magic_trick.out",ofstream::out);
    in.open("A-small-attempt0.in",ifstream::in);
    int T;
    in>>T;
    for(int ii=0;ii<T;++ii)
    {
        int choice1,choice2;
        in>>choice1;
        vector<vector<int> > card1(4,vector<int> (4));
        vector<vector<int> > card2(4,vector<int> (4));
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                in>>card1[i][j];
        in>>choice2;
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                in>>card2[i][j];
        sort(card1[choice1-1].begin(),card1[choice1-1].end());
        int found = 0;int card_num = 0;
        for(int i=0;i<4;++i)
            if(binary_search(card1[choice1-1].begin(),card1[choice1-1].end(),card2[choice2-1][i]))
            {
                    found++;
                    card_num = card2[choice2-1][i];
            }
        ou<<"Case #"<<ii+1<<": ";
        if(found==1)
            ou<<card_num<<"\n";
        else if(found == 0)
            ou<<"Volunteer cheated!\n";
        else
            ou<<"Bad magician!\n";
    }
}
