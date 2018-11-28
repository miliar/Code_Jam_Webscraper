#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;
/*double D;
    long long N,A;
    double carDistanse[2000];
    double carTime[2000];
    double acc[250];

double getMinTime(double accelaration){
    double time,minTime;
    minTime=sqrt(2*D/accelaration);
    double max=0;
    for(int i=0;i<N;i++){
        time=carTime[i]-(sqrt(2*carDistanse[i]/accelaration));
        if(time>max)max=time;

    }
    return minTime+max;
}*/
int status[10000];
long long X,Y;
char *answer;
long long total;
bool generatePartAnswer(long long east,long long west,long long north,long long south,long long N){
    if((east|west|north|south)==0)
    return true;
    int i=0;
    while(i<N&&answer[i]!='A')i++;
    i++;
    if(east>0&&east<i)return false;
    if(west>0&&west<i)return false;
    if(north>0&&north<i)return false;
    if(south>0&&south<i)return false;
    if(east>0){
        answer[i-1]='E';
        if(generatePartAnswer(east-i,west,north,south,N))
        return true;

    }if(west>0){
        answer[i-1]='W';
        if(generatePartAnswer(east,west-i,north,south,N))
        return true;

    }if(north>0){
        answer[i-1]='N';
        if(generatePartAnswer(east,west,north-i,south,N))
        return true;

    }if(south>0){
        answer[i-1]='S';
        if(generatePartAnswer(east,west,north,south-i,N))
        return true;

    }return false;

}
bool generateAnswer(long long N){
    long long M=N*(N+1)/2;
    if(M<total||(M-total)%2!=0)
    return false;
    answer=new char[N+1];
    for(int i=0;i<N;i++)answer[i]='A';
    long long east=X;
    long long west=0;
    long long south=(M-X-Y)/2;
    long long north=M-south-east;
    while(south>-1){
        if(generatePartAnswer(east,west,north,south,N))
        return true;
        east++;west++;
        north--;south--;
    }


}
int main()
{
    int test_cases;
    freopen("g:/input.txt","r",stdin);
    freopen("g:/output.txt","w",stdout);
    cin>>test_cases;
    long long P,Q;
    string fraction;
   for(int caseNum=0;caseNum<test_cases;caseNum++){
       cin>>fraction;
       P=0;Q=0;
       int i=0;
       while(fraction[i]!='/'){
           P=P*10+(fraction[i]-'0');
           i++;
       }
       i++;
       int len=fraction.size();
       while(i<len){
           Q=Q*10+(fraction[i]-'0');i++;
       }
       for(int j=2;j<=P;j++){
           while(P%j==0&&Q%j==0){
               P/=j;
               Q/=j;
           }
       }
       int k=0;
       while(Q%2==0&&Q>P){
           Q/=2;k++;
       }
       while(Q%2==0){
           Q/=2;
       }

        cout<<"Case #"<<caseNum+1<<": ";//<<endl
       // printf("\n%.8lf",getMinTime(acc[i]));
       //cout<<answer;
       if(Q==1)cout<<k;
       else cout<<"impossible";
        cout<<endl;
  }
    return 0;
    }


