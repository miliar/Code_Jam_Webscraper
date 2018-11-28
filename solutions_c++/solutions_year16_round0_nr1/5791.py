#include<iostream>
#include<fstream>
using namespace std;
main()
{
    ifstream input("A-large.in");
    ofstream out("output.txt");
    long long N,c=0;
    int rr;
    input>>rr;
    for(int yy=0;yy<rr;yy++){
    long long arr [10]={1,0,0,0,0,0,0,0,0,0};
    long long counter=0;
    long long pd=1,result,res;
    input>>N;
    if(N==0){
    	c++;
		out<<"Case #"<<c<<":"<<" INSOMNIA"<<endl;
    	continue;
	}
   	while(1){
    	counter=0;
        result=N*pd;
        while(result!=0)
        {
            res=result%10;
            arr[res]=res;
            result=result/10;
        }
        for(int i=0;i<10;i++)  // chick point
        {
			if(arr[i]==i){
				counter++;
			}
        }
            if(counter==10){
				c++;
				out<<"Case #"<<c<<": "<<N*pd<<endl;
				break;
			}
        pd++;
		}
	}   
}


