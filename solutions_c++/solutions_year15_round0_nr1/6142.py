#include <stdio.h>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main()
{
    int T;
    //scanf("%d",&T);
    int cas=1;
    char ss[2000]={'0'};
    int sss[2000]={0};
    int S;
    int i,j;
    int temp1;
    int temp2;
    int sum;
    int max;
        temp1=0;
        sum=0;
        ifstream fin("A-large.in",ifstream::in);
        if(!fin)
          return EXIT_FAILURE;
        ofstream fout("out.out",ofstream::out);
        //scanf("%d",&S);
        //while(fin.peek() != EOF)
        //{
        fin>>T;
        while(T--)
        {
            max=0;
            sum=0;
        memset(ss,'0',sizeof(ss));
        memset(sss,0,sizeof(sss));
        fin>>S;
        for(i=0;i<=S;i++)
        {
            fin>>ss[i];
            sss[i]=ss[i]-'0';
        }
        //temp2=ss[0]-'0';
        for(j=1;j<=S;j++)
        {
            sum=0;
        for(i=0;i<j;i++)
        {

            sum+=sss[i];
        }
        if(sum<j&&ss[j]!='0')
        {
            ss[0]+=(j-sum);
            if((j-sum)>max)
            {
                max=j-sum;
            }
        }
        }
        fout<<"Case #"<<cas++<<": "<<max<<endl;
        //cout<<"Case #"<<cas++<<": "<<max<<endl;
        }
        //}
    return 0;
}
