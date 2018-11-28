#include<iostream>
#include<fstream>
#include<cstring>
#include<vector>
#include<algorithm>
#define cin ifile
#define cout ofile      //Z 0 ,g8, 4u,2w, 6x,
                         // R 3, O 1, S 7,  5 V,I 9
using namespace std;

char arr[][12]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
char str[3000];
vector<int> ans;

int cnt[26];

void upd(int ind,int k)
{
    for(int i=0;arr[ind][i]!='\0';i++)
    {
        cnt[arr[ind][i]-'A']-=k;
    }
    for(int i=0;i<k;i++)
    {
        ans.push_back(ind);
    }
}

int main()
{
    ifstream ifile;
    ifile.open("A-large.in");
    ofstream ofile;
    ofile.open("output1.txt");
    int t;
    cin>>t;

    for(int v=1;v<=t;v++)
    {
        for(int i=0;i<26;i++)
            cnt[i]=0;
        ans.clear();
        cin>>str;
        for(int i=0;str[i]!='\0';i++)
        {
            cnt[str[i]-'A']++;
        }

        //ZERO
        int k=cnt['Z'-'A'];
        upd(0,k);

        //EIGHT
         k=cnt['G'-'A'];
         upd(8,k);

         //FOUR
         k=cnt['U'-'A'];
         upd(4,k);

         //two
         k=cnt['W'-'A'];
         upd(2,k);

         //siz
         k=cnt['X'-'A'];
         upd(6,k);

         //three
         k=cnt['R'-'A'];
         upd(3,k);

         //one
         k=cnt['O'-'A'];
         upd(1,k);

         //seven
            k=cnt['S'-'A'];
         upd(7,k);
         //five
         k=cnt['V'-'A'];
         upd(5,k);
         //nine
         k=cnt['I'-'A'];
         upd(9,k);

         sort(ans.begin(),ans.end());
        cout<<"Case #"<<v<<": ";
        for(int i=0;i<ans.size();i++)
            cout<<ans[i];
        cout<<endl;

    }

    return 0;
}
