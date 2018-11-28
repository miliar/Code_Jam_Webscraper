//#include<cstdio>
//#include<iostream>
//#include<algorithm>

#include<stdio.h>
//#include <fstream>
#include <string.h>

//using namespace std;

int main()
{
    char S1[101],S2[101];
    int T,cnt1,cnt2,count;
    scanf("%d",&T);
    //ofstream out;
	//out.open("output.txt",ios::out);
	//ifstream in;
	//in.open ("Sample.txt",ios::in);

    while(T--)
    {
        scanf("%s",&S1);
        scanf("%s",&S2);
        int i=0,j=0;
        if(S1[0]==S2[0])
        {
            count=0;
            while(i<strlen(S1)&&j<strlen(S2))
            {
                cnt1=0;cnt2=0;
                while(S1[i]==S1[i+1])
                {
                    cnt1++;
                    i++;
                }
                while(S2[j]==S2[j+1])
                {
                    cnt2++;
                    j++;
                }
                if(cnt1>cnt2)
                    count=cnt1-cnt2;
                else
                    count=cnt2-cnt1;
                i++;j++;
                int d=0;
                if(S1[i]!=S2[j])
                {
                     d=1;
                    break;
                }
                if(d==1)
                    printf("fegla won\n");
                else
                    printf("%d\n",count);
            }
        }
        else
            printf("fegla won\n");
    }
    return 0;
}
