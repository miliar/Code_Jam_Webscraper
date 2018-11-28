#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
int t,c;
string num;
int wcount[27],numcount[10];
//long long int n,res;
cin>>t;
for(int i=0;i<t;i++){
memset(wcount,0,sizeof(wcount));
memset(numcount,0,sizeof(numcount));
cin>>num;
for(int j=0;j<num.size();j++)
    {
    wcount[num[j]-'A']++;
    }
//for(int b=0;b<26;b++){if(wcount[b]>0)cout<<wcount[b]<<endl;}
c=0;
if(c=wcount[25]!=0){            //0z
    c=wcount[25];
    wcount[4]-=c;
    wcount[14]-=c;
    wcount[17]-=c;
    wcount[25]=0;
    numcount[0]=c;
    }
if(c=wcount[22]!=0){            //2w
    c=wcount[22];
    wcount[19]-=c;
    wcount[14]-=c;
    wcount[22]=0;
    numcount[2]=c;
}
if(c=wcount[20]!=0){            //4u
    c=wcount[20];
    wcount[5]-=c;
    wcount[14]-=c;
    wcount[17]-=c;
    wcount[20]=0;
    numcount[4]=c;
    }
if(c=wcount[23]!=0){            //6x
    c=wcount[23];
    wcount[18]-=c;
    wcount[8]-=c;
    wcount[23]=0;
    numcount[6]=c;
}
if(c=wcount[6]!=0){            //8g
    c=wcount[6];
    wcount[4]-=c;
    wcount[7]-=c;
    wcount[8]-=c;
    wcount[19]-=c;
    wcount[6]=0;
    numcount[8]=c;
}
if(c=wcount[14]!=0){        //1o

    c=wcount[14];
    wcount[4]-=c;
    wcount[13]-=c;
    wcount[14]=0;
    numcount[1]=c;
    }
if(c=wcount[7]!=0){     //3h
    c=wcount[7];
    wcount[4]-=2*c;
    wcount[19]-=c;
    wcount[17]-=c;
    wcount[7]=0;
    numcount[3]=c;
}
if(c=wcount[5]!=0){     //5f
    c=wcount[5];
    wcount[4]-=c;
    wcount[8]-=c;
    wcount[16]-=c;
    wcount[5]=0;
    numcount[5]=c;
}
if(c=wcount[18]!=0){        //7s
    c=wcount[18];
    wcount[4]-=2*c;
    wcount[21]-=c;
    wcount[13]-=c;
    wcount[18]=0;
    numcount[7]=c;
}
if(c=wcount[8]!=0){      //9n
    c=wcount[8];
    wcount[13]-=2*c;
    wcount[4]-=c;
    wcount[8]=0;
    numcount[9]=c;
}
printf("Case #%d: ",i+1);
for(int p=0;p<10;p++){
    if(numcount[p]>0){
            c=numcount[p];
            for(int q=0;q<c;q++){
            cout<<p;
            }
        }
    }
cout<<endl;
}


return 0;
}
