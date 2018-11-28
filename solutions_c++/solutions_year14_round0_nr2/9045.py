#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

void solve();
void response(double,double,double,int);

int main(){
    solve();
    return 0;
}

void solve(){
    int n;
    double c,f,x;
    cout<<setiosflags(ios::fixed)<<setprecision(7);
    cin>>n;
    for(int i = 1;i<n+1;i++){
        cin>>c>>f>>x;
        response(c,f,x,i);
    }
}

void response(double c,double f, double x,int caseN){
    double spent=0,willspend=0,answer=1,time=0,rate=2;
    double answerOld = 1000000;
    if(c<x){
        do{
            answerOld = time+x/rate;
            spent+=c;
            time+=c/rate;
            rate+=f;
            answer = time+x/rate;
        }while(answerOld > answer);
        answer = answerOld;
    }else{
        answer=x/rate;
    }
    ofstream output;
    output.open("output.txt",ios_base::app);
    output<<"Case #"<<setprecision(20)<<caseN<<": "<<answer<<endl;
}
