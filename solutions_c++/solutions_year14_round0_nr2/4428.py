#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
#include<iostream>
using namespace std;


int main(){
//	READ("B-large.in");
   // WRITE("B-large.out");
	long double timer=0,x,c,f;
	long double pro=2,num;
    cin>>num;
    for(int i=0;i<num;i++){
       cin>>c>>f>>x;
       timer=0;
       pro=2;
       while(1){
          if(timer+(x/pro)<timer+((c/pro)+(x/(pro+f)))){
              timer+=(x/pro);
            // cout<<"timer "<<timer<<endl;
	           break;
          } 
          else{
        	timer+=(c/pro);
        //	cout<<"timer "<<timer<<endl;
        	pro+=f;
          } 
	 
	
	   }
	   cout.precision(7);
       cout.setf( std::ios::fixed, std:: ios::floatfield );
	   cout<<"Case #"<<i+1<<": "<<timer<<endl;
		
	
    } 
	
}
