#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
    ofstream ans;
    ifstream que;
    que.open("C:\\Codejam\\A-small-attempt1.in");
    ans.open("C:\\Codejam\\output.txt");

    int T;
    int initmatrix[4][4];
    int finmatrix[4][4];
    int check[]={0,0,0,0};
    int check2[]={0,0,0,0};
    int p=1;
    int n,i,j;

    que>>T;
    while(T--)
    {
        que>>n;
        for(i=0;i<4;i++)
                for(j=0;j<4;j++)
                    que>>initmatrix[i][j];

        for(j=0;j<4;j++)
                check[j]=initmatrix[n-1][j];

        que>>n;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                que>>finmatrix[i][j];

        for(j=0;j<4;j++)
                check2[j]=finmatrix[n-1][j];

        sort(check,check+4);
        sort(check2,check2+4);

        vector<int> v(5);
        vector<int>::iterator it;
        it=set_intersection(check,check+4,check2,check2+4,v.begin());
        v.resize(it-v.begin());

        ans<<"Case #"<<p++<<": ";
        if(v.size()==1)
            ans<<v[0]<<"\n";
        else if(v.size()==0)
            ans<<"Volunteer cheated!\n";
        else
            ans<<"Bad magician!\n";

    }
    ans.close();
    return 0;
}
