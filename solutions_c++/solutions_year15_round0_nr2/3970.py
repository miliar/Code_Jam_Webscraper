#include <bits/stdc++.h>
using namespace std;
int input[1001];
int minimun(int a,int b){
    if(a>b)return b;
    else return a;
}
void sort(int n){
    int a,i,j;
    for (i = 0; i < n; ++i)
    {
        for (j = i + 1; j < n; ++j)
        {
            if (input[i] < input[j])
            {
                a =  input[i];
                input[i] = input[j];
                input[j] = a;
            }
        }
    }
}

int main()
{
    int t,final[9],length;
    cin>>t;
    for (int i = 0; i < t; i++) {
        cin>>length;
        for (int l = 0; l < length; l++) {
            cin>>input[l];
        }
        int flag=1;
        sort(length);
        int max_char=input[0];
        int final=max_char,n=length;
        if(max_char>2)
        for(int k = 1 ; k <= max_char;++k){
            int time = 0;
            for(int j=0;j<n;++j){
        		time += (input[j]-1)/k;
        	}
        	time+=k;
        	final=minimun(final,time);
        }
        cout<<"Case #"<<i+1<<": "<<final<<endl;
    }
    return 0;
}

