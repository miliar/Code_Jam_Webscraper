#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
    int t,c;
    cin>>t;
    c=1;
    int num[1005];
    int left_large, right_large;
    int i,j,k;
    int max_num;
    int n,max_pos;
    while(c<=t)
    {
        cin>>n;
        max_num=-1;
        max_pos=-1;
        for(i=0; i<n; i++)
        {
            cin>>num[i];
            if(num[i]>max_num)
            {
                max_num = num[i];
                max_pos = i;
            }
        }
        int count=0;
        for(i=max_pos-1; i>=0;)
        {
            left_large=0;
            right_large=max_pos-i;
            for(k=0;k<i;k++)
                if(num[k]>num[i])
                    left_large++;
            for(k=max_pos+1; k<n; k++)
                if(num[k]>num[i])
                    right_large++;
            if(right_large<left_large)
            {
                int mid=num[i];
                for(k=i;k<max_pos;k++)
                    num[k]=num[k+1];
                num[max_pos]=mid;
                count+=max_pos-i;
                max_pos--;
            }
            else
                i--;
        }
        for(i=max_pos+1; i<n;)
        {
            left_large=i-max_pos;
            right_large=0;
            for(k=0;k<max_pos;k++)
                if(num[k]>num[i])
                    left_large++;
            for(k=i; k<n; k++)
                if(num[k]>num[i])
                    right_large++;
            if(right_large>left_large)
            {
                int mid=num[i];
                for(k=i;k>max_pos;k--)
                    num[k]=num[k-1];
                num[max_pos]=mid;
                count+=i-max_pos;
                max_pos++;
            }
            else
                i++;
        }

        for(i=0;i<max_pos;i++)
        {
            for(j=i+1; j<max_pos; j++)
            {
                if(num[i]>num[j])
                    count+=1;
            }
        }
        for(i=max_pos+1; i<n; i++)
        {
            for(j=i+1; j<n; j++)
            {
                if(num[i]<num[j])
                    count+=1;
            }
        }

        cout<<"Case #"<<c<<": "<<count<<endl;
        c++;
    }
    return 0;
}

