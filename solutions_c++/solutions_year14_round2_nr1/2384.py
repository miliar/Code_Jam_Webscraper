#include <iostream>
#include <cstdio>
#include<fstream>
#include <algorithm>
#include <vector>
#include <cstring>
//# define abs(x) x<0?-x:x
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("D:\in.txt");
    fout.open("D:\out.txt");
    char c1[1001],c2[1001],ch;
    int t,n,i,z;
   // scanf("%d",&t);
   fin>>t;
    for(z=1;z<=t;z++)
    {
        int count1=1,count2=1,result=0,flag=0;
        //scanf("%d",&n);
        //scanf("%s",c1);
        //scanf("%s",c2);
        fin>>n;
        fin>>c1;
        fin>>c2;
        for(i=0;c1[i]!='\0';i++)
        {
            if(i==0)    ch=c1[i];
                else if(c1[i]!=ch)  {   count1++;   ch=c1[i];    }
        }
        for(i=0;c2[i]!='\0';i++)
        {
            if(i==0)    ch=c2[i];
                else if(c2[i]!=ch)  {   count2++;   ch=c2[i];    }
        }
        pair <char,int> p1[count1],p2[count1];
        if(count1==count2)
        {
            //pair <char,int> p1[count1],p2[count1];
            for(i=0;i<count1;i++)
            {
                p1[i].second=0;
                p2[i].second=0;
            }
            int k=0;
            for(i=0;c1[i]!='\0';i++)
            {
                if(i==0)    {   p1[0].first=c1[i];      p1[0].second++;         }
                else if(c1[i]==c1[i-1])   p1[k].second++;
                else if(c1[i]!=c1[i-1])   { k++;  p1[k].first=c1[i];      p1[k].second++; }
            }
            k=0;
            for(i=0;c2[i]!='\0';i++)
            {
                if(i==0)    {   p2[0].first=c2[i];      p2[0].second++;         }
                else if(c2[i]==c2[i-1])   p2[k].second++;
                else if(c2[i]!=c2[i-1])   { k++;  p2[k].first=c2[i];      p2[k].second++; }
            }
            for(i=0;i<count1;i++)
            {
                if(p1[i].first==p2[i].first)
                {
                    if(p1[i].second>p2[i].second)
                        result+=(p1[i].second-p2[i].second);
                    else
                        result+=(p2[i].second-p1[i].second);
                }
                else
                {
                    flag=1;
                    break;
                }
            }
        }
        else
            flag=1;
        if(flag==0)
            //printf("Case #%d: %d\n",z,result);
            fout<<"Case #"<<z<<": "<<result<<"\n";
        else
           fout<<"Case #"<<z<<": Fegla Won\n";
           // printf("Case #%d: Fegla Won\n",z);
        /*for(i=0;i<count1;i++)
            printf("%c %d\n",p1[i].first,p1[i].second);
        printf("\n");
        for(i=0;i<count1;i++)
            printf("%c %d\n",p2[i].first,p2[i].second);*/
    }

}
