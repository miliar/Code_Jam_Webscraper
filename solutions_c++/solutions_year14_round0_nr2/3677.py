#include<iostream>
#include <limits>
#include<fstream>
#include<iomanip> 
#include <vector>
using namespace std;

int main(){
	int t;   
    long double caseseq[100];//1 succeed 0 Volunteer cheated!(no)  -1 Bad magician!(mul)
    long double C;
    long double X;
    long double F;
    long double time=0;
    long double rate;
    
    fstream fin;
    fin.open("D:\\Users\\Ebrai\\Documents\\NetBeansProjects\\Problem A. Minimum Scalar Product\\in.txt");
    fin>>t;
    fstream fout;
    fout.open("D:\\Users\\Ebrai\\Documents\\NetBeansProjects\\Problem A. Minimum Scalar Product\\out.txt");
    
    for(int i=0;i<t;i++){
        fin >> C;
        fin >> F;
        fin >> X;
        
        double long time=0.0;
        double long cookies = 0.0;
        double long  farms = 0;
        double long rate=2;
        while(cookies < X){
            rate = 2 + farms*F ;
            if((cookies + C) > X){
                time += (X - cookies)/rate;
                cookies =X;
                break;
            }
            else{
                time += C/rate;
                cookies += C;
            }
            if( (X+C-cookies)/(rate + F) < (X-cookies)/rate){
                farms++;
                cookies -= C;
            }
        }
    //    cout<<"time "<<time<<endl;
        caseseq[i] = time;
      //  fout << "Case #"<<i+1 <<fixed<<setprecision(7)<< ": "<<caseseq[i]<<"\r\n";
    //    cout<<"csae "<<"i  "<<i<<" " <<caseseq[i]<<endl;
  
    }
    fin.close();
for( int i=0;i<t;i++){
    	
    	//cout<<"csae in fout  "<<caseseq[i]<<endl;
        fout << "Case #"<<i+1 <<fixed<<setprecision(7)<< ": "<<caseseq[i]<<"\r\n";
    }

    	
  return 0;
}
