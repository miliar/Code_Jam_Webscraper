//DEEPAK AHIRE
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <bitset>
#include <vector>
#include <cstdio>
#include <string>
#include <cassert>
#include <climits>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <fstream>
using namespace std;
#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define abs(x) ((x) > 0 ? (x) : -(x))
#define FOREACH(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
typedef long long int LL;
#define INF 1000001

#define IF 1000000000000000L

char arr[101];

int check(char arr[])
{
    //cout<<"Arr:"<<arr;
    int i=0,len = strlen(arr);
    for(i=0;i<len;i++)
        if(arr[i] != '+')
        break;

    return i==len;
}
void swaparr(char * arr , int st ,int en)
{
    int i,mid = (st+en)/2;
    int st1=st;
    int en1=en;
    for(i=st1;i<=mid;i++)
    {
        char temp = arr[i];
        arr[i] = arr[en1];
        arr[en1] = temp;
        en1--;
    }

    for(i=st;i<=en;i++)
    {
        if(arr[i]=='+')
            arr[i]='-';
        else
            arr[i]= '+';
    }

}
int main()
{
     ofstream myfile;
    myfile.open ("3.txt");
    int t,index,cnt,i,len,flg,c;
    cin>>t;
    c=1;
    while(t--)
    {
        cin>>arr;
        int length = strlen(arr);
        int s=3;
        cnt=0;
        while(1)
        {
            flg=0;
            if(check(arr))
                break;
            //
            len=0;
            for(i=length-1; ; i--)
            {
                if(arr[i] == '+')
                {
                    len++;
                }
                else
                    break;
            }
            length -= len;
            //
            //cnt=0;
            len=0;
            for(i=0;i<length;i++)
            {
                if(arr[i]=='+')
                   {
                        len++;
                   }
                else
                    break;
            }
            for(i=0;i<len;i++)
            {
                flg=1;
                arr[i]='-';
            }
            if(flg)
            cnt++;

            len=0;
            for(i=0; ;i++)
            {
                if(arr[i]=='-')
                {
                    len++;
                }
                else
                    break;
            }
            swaparr(arr,0,length-1);
            cnt++;//cout<<cnt<<endl;
            //cout<<arr<<endl;
            length -= len;



        }
        myfile<<"Case #"<<c++<<": "<<cnt<<endl;
    }
    return 0;
}
