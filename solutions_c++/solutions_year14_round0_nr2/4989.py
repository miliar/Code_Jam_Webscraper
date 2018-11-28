#include <iostream>

using namespace std;

int main(void){
int t,farm;
double c,f,x;
double time;
cin>>t;
for(int n=1;n<=t;n++){
    cin>>c>>f>>x;
    farm=0;
    time=0;
    while((x/(2+f*farm)) > (c/(2+f*farm)+x/(2+f*(farm+1)))){
        time += c/(2+f*farm);
        farm++;
    };
    time += x/(2+f*farm);
    cout.setf(ios::showpoint);
    cout.precision(7);
    cout.setf(ios::fixed);
    cout<<"Case #"<<n<<": "<<time<<endl;
}
return 0;
}
