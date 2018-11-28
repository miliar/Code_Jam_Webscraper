#include <iostream>
#include <stdio.h>
#include <map>
#include <vector>
#include <string.h>
using namespace std;

int t;
string word;
map<string,int> mymap;
map<string,int>::iterator myit;
int idctr=0;
vector<int> words[222];
vector<int> whereis[22222];

void AddEdge()
{

}

int main()
{
    freopen("C-small-attempt2-2.in","r",stdin);
    freopen("C-small-output-2.txt","w",stdout);

    int test;
    char ch;
    int id;
    int i,j,in;
    int n;
    int mask;
    bool has0,has1;
    int ans=0;
    int minans;
    int beg;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        fprintf(stderr,"%d\n",test);

        scanf("%d",&n);
        scanf("%c",&ch);

        for (i=1;i<=n;i++)
        {
            words[i].clear();
        }
        for (i=1;i<=20000;i++)
        {
            whereis[i].clear();
        }

        for (i=1;i<=n;i++)
        {
            word.clear();

            while(1)
            {
                if ( scanf("%c",&ch)!=1 )
                ch='#';

                if (ch==' ')
                {
                    myit=mymap.find(word);

                    if (myit==mymap.end())
                    {
                        idctr++;
                        id=idctr;
                        mymap.insert(make_pair(word,id));
                    }
                    else
                    id=(*myit).second;

                    words[i].push_back(id);
                    whereis[id].push_back(i);

                    word.clear();
                }
                else if (ch>='a' && ch<='z')
                {
                    word.push_back(ch);
                }
                else
                {
                    myit=mymap.find(word);

                    if (myit==mymap.end())
                    {
                        idctr++;
                        id=idctr;
                        mymap.insert(make_pair(word,id));
                    }
                    else
                    id=(*myit).second;

                    words[i].push_back(id);
                    whereis[id].push_back(i);

                    word.clear();

                    break;
                }
            }
        }

        ans=0;
        minans=999999;
        if (n<4)
        beg=0;
        else
        beg=(1<<(n-3));

        for (mask=beg;mask<(1<<(n-2));mask++)
        {
            ans=0;
            for (i=1;i<=idctr;i++)
            {
                has0=false;
                has1=false;
                for (j=0;j<whereis[i].size();j++)
                {
                    if (whereis[i][j]==1)
                    has0=true;
                    else if (whereis[i][j]==2)
                    has1=true;
                    else if ( (mask&(1<<(whereis[i][j]-3)))==0 )
                    has0=true;
                    else
                    has1=true;

                    if (has0 && has1)
                    break;
                }

                if (has0 && has1)
                {
                    ans++;
                }

                if (ans>=minans)
                break;
            }

            if (ans<minans)
            {
                minans=ans;
            }
        }

        //printf("Case #%d: %d\n",test,minans);
        printf("%d\n",minans);
    }

    return 0;
}
