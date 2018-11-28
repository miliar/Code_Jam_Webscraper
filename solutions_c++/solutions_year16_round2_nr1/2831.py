#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){
    freopen("1b.in","r",stdin);
    freopen("1b2.out","w",stdout);
    int t,n,i,j;
    string s;
    cin>>t;
    for(i=1;i<=t;i++){
            cin>>s;
   int ar[26]={0};
   int a[10]={0};
    for(j=0;j<s.length();j++){
    ar[s[j]-65]++;
    }
          //zero
        if(ar[25]!=0){
            a[0]=ar[25];
            ar[4]-= ar[25];
            ar[17]-= ar[25];
            ar[14]-= ar[25];
            ar[25]=0;
        }//six
        if(ar[23]!=0)
        {   a[6]=ar[23];
            ar[8]-= ar[23];
            ar[18]-= ar[23];
            ar[23]=0;
        }
        //two
        if(ar[22]!=0)
        {   a[2]=ar[22];
            ar[19]-= ar[22];
            ar[14]-= ar[22];
            ar[22]=0;
        }
        //eight
        if(ar[6]!=0)
        {   a[8]=ar[6];
            ar[4]-= ar[6];
            ar[8]-= ar[6];
            ar[7]-= ar[6];
            ar[19]-= ar[6];
            ar[6]=0;
        }
        //three
        if(ar[7]!=0)
        {   a[3]=ar[7];
            ar[19]-= ar[7];
            ar[4]-= (2*ar[7]);
            ar[17]-= ar[7];
            ar[7]=0;
        }
        //four
        if(ar[17]!=0)
        {   a[4]=ar[17];
            ar[5]-= ar[17];
            ar[14]-= ar[17];
            ar[20]-= ar[17];
            ar[17]=0;
        }
        //five
        if(ar[5]!=0)
        {   a[5]=ar[5];
            ar[8]-= ar[5];
            ar[21]-= ar[5];
            ar[4]-= ar[5];
            ar[5]=0;
        }
        //seven
        if(ar[21]!=0)
        {   a[7]=ar[21];
            ar[13]-= ar[21];
            ar[4]-= (2*ar[21]);
            ar[18]-= ar[21];
            ar[21]=0;
        }
        //nine
        if(ar[8]!=0)
        {   a[9]=ar[8];
            ar[4]-= ar[8];
            ar[13]-= (2*ar[8]);
            ar[8]=0;
        }
        //one
        if(ar[14]!=0)
        {   a[1]=ar[14];
            ar[13]-= ar[14];
            ar[4]-= ar[14];
            ar[14]=0;
        }
         cout<<"Case #"<<i<<": ";
        for(j=0;j<10;j++)
        while(a[j]--)
            cout<<j;
        cout<<endl;

    }
return 0;
}
