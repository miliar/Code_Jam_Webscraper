#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> arr;
void fn(int chk_arr[],int c,int d,int v)
    {
    d=arr.size();
    int check=pow(2,d)-1;
        for(int i=0;i<=check;i++)
            {
            int binary[d]={0};
            int c=0;
            int sum=0;
            int temp=i;
            while(temp)
                {
                binary[c++]=temp%2;
                temp/=2;
            }
            for(int k=0;k<d;k++)
                {
                if(binary[k]==1)
                    {
                    sum+=arr[k];
                }
            }
            if(sum<=v)
                chk_arr[sum]=1;
            
        }
}
int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin>>t;
    for(int cases=1;cases<=t;cases++)
        {
        int c,d,v;
        cin>>c>>d>>v;
        //vector<int> arr(d);
        arr.resize(d);
        for(int i=0;i<d;i++)
            cin>>arr[i];
        int chk_arr[v+1]={0};
        chk_arr[0]=1;
        int count=0;
    //     int curr_sum, i, j;
 
         
        while(1)
        {
            int add=-1;
            fn(chk_arr,c,d,v);
        
            for(int i=0;i<=v;i++)
        {//cout<<"\ni "<<i<<" "<<chk_arr[i];
         if(chk_arr[i]!=1)
         {add=i;break;}
        }
            if(add==-1)
                break;
            else
            {arr.push_back(add);count++;}
        }
    // cout<<count<<"\n";
        cout<<"Case #"<<cases<<": "<<count<<"\n";

    }


    return 0;
}