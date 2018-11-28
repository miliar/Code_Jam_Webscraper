#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <queue>

using namespace std;

int main()
{
	ifstream ifs("D-large.in");
    ofstream ofs("answer");
	int T;
	ifs >> T; cout << "T= " << T <<endl;
   
   for(int t=0;t<T;t++){  // test cases
	int N;
    ifs >> N; cout << "N= " << N << endl; 

	vector <double> V1,V2;
	double dummy;

	for(int i=0;i<N;i++){
         ifs >> dummy;  //cout << " " <<dummy;
		 V1.push_back(dummy);
	}
  //cout <<endl;
    for(int i=0;i<N;i++){
         ifs >> dummy; //cout << " " <<dummy;
		 V2.push_back(dummy);
	}
	//cout <<endl;

	sort(V1.begin(),V1.end());
	for(int i=0;i<N;i++){
      cout <<" " <<V1[i];
	}
    cout <<endl;


    sort(V2.begin(),V2.end());
	for(int i=0;i<N;i++){
      cout <<" " <<V2[i];
	}
	cout <<endl;

//================== y ===================//

	vector<double> d1,d2;
	d1=V1; d2=V2;
	double d1_max,d2_max;
	d1_max=d1[N-1]; d2_max=d2[N-1]; //cout <<"d1_max= " << d1_max <<endl;
	                                //cout <<"d2_max= " << d2_max <<endl;
	vector<double> temp;
	while(d1_max<d2_max){
      temp.clear();
	  for(int i=1;i<int(d1.size());i++){
        temp.push_back(d1[i]);
	  }
	    d1=temp;
	    d2.pop_back();
		if(int(d1.size())==0){break;}
		else{ d1_max=d1[int(d1.size())-1];
		      d2_max=d2[int(d2.size())-1];
		}
	}

/*	for(int i=0;i<int(d1.size());i++){
		cout << " " << d1[i];
	}
   cout <<endl;

   for(int i=0;i<int(d2.size());i++){
		cout << " " << d2[i];
	}
   cout <<endl;*/

   int ans=0;

   for(;;){
	   if(d1.size()==0){break;}
	   if(d1[0]<d2[0]){    temp.clear();
	                    for(int i=1;i<int(d1.size());i++){
	                        temp.push_back(d1[i]); 
						 }
						d1=temp;
                        d2.pop_back();
	   }else{
                 temp.clear();
				 for(int i=1;i<int(d1.size());i++)
				 {    temp.push_back(d1[i]);
				 }
				 d1=temp;
				 temp.clear();
				 for(int i=1;i<int(d2.size());i++){
                       temp.push_back(d2[i]);
				 }
				 d2=temp;
                 ans++;
	   } 
   }//inf-loop

   //cout <<"ans= " <<ans <<endl;

   //--------------------------- z ----------------------//

   int z=N;
   d1=V1; d2=V2;
   for(int i=0;i<int(d1.size()); i++){
	   int J_ex=0;  //cout << "d1.size= " <<d1.size() <<endl;
	   for(int j=0; j<int(d2.size());j++){
		   if(d1[i]<d2[j]){J_ex=j;z--;break;}
	   }//j-loop

        temp.clear();
		for(int j=0;j<int(d2.size());j++){
			if(j==J_ex){continue;}
			else{
                temp.push_back(d2[j]);
			}
		}
		d2=temp;

   }//i-loop


   //cout <<"z= " <<z <<endl;

	cout << "Case #" <<t+1<<": " <<ans << " " << z <<endl;
    ofs << "Case #" <<t+1<<": " <<ans << " " << z <<endl;

   } // end of test cases

 return 0;
}