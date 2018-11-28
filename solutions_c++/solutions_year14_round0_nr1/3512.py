#include<cstdio>
#include<vector>
using namespace std;/*
void p(vector<int > v)
{
    for(int i=0;i<v.size();i++)
        printf("%d ",v[i]);
    printf("\n");
}*/
vector<int> common(vector<int> a,vector<int> b)
{
 //   p(a);
   // p(b);
    vector<int> ret;
    for(int i=0;i<a.size();i++)
        for(int j=0;j<b.size();j++)
            if(a[i]==b[j])
            {
                ret.push_back(a[i]);
            }
    return ret;
}

int main()
{
    freopen("as.in","r",stdin);
    freopen("a.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int test=0;test<t;test++)
    {
        int row[2];
        vector<vector<int> > in[2];
        for(int i=0;i<2;i++)
        {
            scanf("%d",&row[i]);
            for(int j=0;j<4;j++)
            {
                vector<int> temp;
                for(int k=0;k<4;k++)
                {
                    int tm;
                    scanf("%d",&tm);
                    temp.push_back(tm);
                }
                in[i].push_back(temp);
            }
        }
        vector<int> result=common(in[0][row[0]-1],in[1][row[1]-1 ]);
        int size=result.size();
        printf("Case #%d: ",test+1);
        if(size==1)
            printf("%d\n",result[0]);
        else if(size>1)
            printf("Bad magician!\n");
        else
            printf("Volunteer cheated!\n");



    }
    return 0;
}
