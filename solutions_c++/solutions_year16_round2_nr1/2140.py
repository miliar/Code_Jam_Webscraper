#include<bits/stdc++.h>
using namespace std;
string val[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
//                   Z            W               U              X               G

//                        O                R              F

//                                                                        S                  N



int main()
{
    freopen("A-large.in","r+",stdin);
    freopen("out1.txt","w+",stdout);
    int T   , i , e , j  ;
    cin>>T;

    for(e=0;e<T;++e)
    {
        int i ;
        cout<<"Case #"<<e+1<<": ";
        string S;
        cin>>S;

        vector < int > F(26,0);

        for(i=0;i<S.length();++i)
            F[S[i]-'A']++;

        vector < int > ans;

        for(;F['Z'-'A'];)
        {
            for(j=0;j<val[0].length();++j)
                F[val[0][j]-'A']--;
            ans.push_back(0);
        }

        for(;F['W'-'A'];)
        {
            for(j=0;j<val[2].length();++j)
                F[val[2][j]-'A']--;
            ans.push_back(2);
        }


        for(;F['U'-'A'];)
        {
            for(j=0;j<val[4].length();++j)
                F[val[4][j]-'A']--;
            ans.push_back(4);
        }


        for(;F['X'-'A'];)
        {
            for(j=0;j<val[6].length();++j)
                F[val[6][j]-'A']--;
            ans.push_back(6);
        }

        for(;F['G'-'A'];)
        {
            for(j=0;j<val[8].length();++j)
                F[val[8][j]-'A']--;
            ans.push_back(8);
        }


         for(;F['O'-'A'];)
        {
            for(j=0;j<val[1].length();++j)
                F[val[1][j]-'A']--;
            ans.push_back(1);
        }
//        cout<<F['O'-'A']<<endl;
//        for(i=0;i<26;++i)
//                cout<<F[i]<<endl;

         for(;F['R'-'A'];)
        {
            for(j=0;j<val[3].length();++j)
                F[val[3][j]-'A']--;
            ans.push_back(3);
        }

        for(;F['F'-'A'];)
        {
            for(j=0;j<val[5].length();++j)
                F[val[5][j]-'A']--;
            ans.push_back(5);
        }

         for(;F['S'-'A'];)
        {
            for(j=0;j<val[7].length();++j)
                F[val[7][j]-'A']--;
            ans.push_back(7);
        }

         for(;F['N'-'A'];)
        {
            for(j=0;j<val[9].length();++j)
                F[val[9][j]-'A']--;
            ans.push_back(9);
        }
        sort(ans.begin(),ans.end());
        for(auto v:ans)
                cout<<v;
        cout<<'\n';
    }
    return 0;
}
