#include <iostream>
#include<cstdio>
#include <algorithm>
using namespace std;
void ha1(char *b)
{
    int h1[100]={0},i,J;
    for(i=0;b[i]!='\0';i++)
    {
        h1[b[i]-48]++;

    }

    for(J=0;J<=9;J++)
    {
        if(h1[J]!=0)
        {
            //cout<<J;
            //h1[J]--;
            //J=0;
            for(i=0;i<h1[J];i++)
                cout<<J;
        }
    }
    cout<<endl;

}
void has(char *a)
{
    int i,t=0;
    char b[2005]={'\0'};

    int h[200]={0};
    for(i=0;a[i]!='\0';i++)
    {
        h[a[i]]++;
    }

    for(i=0;i<h[90];i++) //zero
    {
        //cout<<h[90];
        b[t++]='0';
        h[69]--;
        h[82]--;
        h[79]--;
    }
     for(i=0;i<h[87];i++) //2
    {
        b[t++]='2';
        h[84]--;
        h[79]--;
    }

    for(i=0;i<h[85];i++) //4
    {
        b[t++]='4';
        h[70]--;
        h[79]--;
        h[82]--;
    }

   for(i=0;i<h[88];i++) //6
    {
        b[t++]='6';
        h[83]--;
        h[73]--;
    }

      for(i=0;i<h[71];i++) //8
    {
        b[t++]='8';
        h[69]--;
        h[73]--;
        h[72]--;
        h[84]--;

    }
     while(h[79]!=0&&h[78]!=0&&h[69]!=0)//1
    {
        b[t++]='1';
        h[79]--;
        h[78]--;
        h[69]--;
    }
     while(h[84]!=0&&h[72]!=0&&h[82]!=0&&h[69]>=2) //3
    {
        b[t++]='3';
        h[72]--;
        h[84]--;
        h[82]--;
        h[69]--;
        h[69]--;
    }
      while(h[70]!=0&&h[73]!=0&&h[86]!=0&&h[69]!=0)//5
    {
        b[t++]='5';
        h[70]--;
        h[73]--;
        h[86]--;
        h[69]--;
    }
    while(h[83]!=0&&h[69]>=2&&h[86]!=0&&h[78]!=0)//7
    {
        b[t++]='7';
        h[83]--;
        h[69]--;
        h[86]--;
        h[69]--;
        h[78]--;
    }


     while(h[73]!=0&&h[78]>=2&&h[69]!=0)//9
    {
        b[t++]='9';
        h[78]--;
        h[73]--;
        h[78]--;
        h[69]--;
    }

ha1(b);

   // cout<<b<<endl;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outputLARGE.txt","w",stdout);
    int t;
    long long int y=1;
    cin>>t;
    while(t--)
    {

        char s[2005]={'\0'},u[2005]={'\0'};
        scanf("%s",s);
        //printf("Case #%lld: %s\n",y++,s);
        printf("Case #%lld: ",y++);
        has(s);


    }
   // cout << "Hello world!" << endl;
    return 0;
}
