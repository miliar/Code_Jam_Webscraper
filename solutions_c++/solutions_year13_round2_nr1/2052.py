#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <sstream>


using namespace std;

#define pb push_back

//g++ -o a.exe a.cpp
//./a.exe < A-small-practice.in > A-small-practice.out

int osmose(int noofmotes,int j, int mote, vector<int> motesv){
	int ans=0;
	int tempans=0;
	while (j<noofmotes){
		if (mote==1){
			ans=noofmotes;
			j=noofmotes;
		}
		else if (motesv.at(j)<mote){
			mote+=motesv.at(j);
			j++;
		}
		else {int tempmote=mote;
			tempans=0;
			//cout<< "comparing  "<<tempmote<< "  and "<<motesv.at(j)<<endl;
			while(tempmote<=motesv.at(j)){
			//		cout<< "checking mul"<<endl;
			tempmote=tempmote*2-1;
			tempans++;
			}
			tempmote+=motesv.at(j);
		
			if (osmose(noofmotes,j+1,mote,motesv)<tempans+osmose(noofmotes,j+1,tempmote,motesv)){
				j++;
			//			cout<<"removing"<<endl;
				ans++;
				
			}
			else{
				mote=tempmote;
			//			cout<<"multiplying "<<tempans<<endl;
       			 ans+=tempans;
       			 j++;
			}
			//int stuck=1;
			//while(stuck!=1){
			//cout << mote<<"  cannot absorb " << motesv.at(j)<<endl;
			//if(motesv.at(j)<2*mote-1){
		//	mote+=mote-1;
				//}
		//	 ans+=1;
		//	 j++;
			// stuck=0;
		// }
		 
		 }
	}
	//cout << "route gives  "<<ans<< " versus "<< tempans<<endl;
	return ans;
}

int cases,mote,noofmotes,motes[10];


int main()
{
	vector<int> motesv;
	int buf,ans;
	cin>> cases;	
		//cout << "begin"<<endl;
		for(int caseno=1;caseno<=cases;caseno++)
		{
			motesv.clear();
			ans=0;
			cin>>mote>>noofmotes;
			
			for (int i=0;i<noofmotes;i++){
				cin>>buf;
				motesv.pb(buf);
				//cout << motesv.at(i)<<endl;
			}
			sort(motesv.begin(),motesv.end());
			int j=0;
			ans=osmose(noofmotes,j,mote,motesv);
			
			
	
			
			
			
			cout <<"Case #"<< caseno<<": "<< ans << endl;
		}
	
	return 0;
}

