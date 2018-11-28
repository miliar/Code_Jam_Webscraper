#include<bits/stdc++.h>
using namespace std;
char arr[102];

int check(char arr[])
{
    long long int i=0,len = strlen(arr);
    for(i=0;i<len;i++)
        if(arr[i] != '+')
        break;

    return i==len;
}
void swaparr(char * arr , int st ,int en)
{
    long long int i,mid = (st+en)/2;
    long long int st1=st;
    long long int en1=en;
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
   FILE *fin = freopen("B-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B-large.out", "w", stdout);
    long long int t,index,cnt,i,len,flg,c;
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
        cout<<"Case #"<<c++<<": "<<cnt<<endl;
    }
    return 0;
}

