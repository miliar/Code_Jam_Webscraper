
#include<vector>
#include<fstream>
#include<iostream>
#include<string>
using namespace std;

class quaternion{
public:
	vector<int> v;
	quaternion(void){
		v.resize(4);
	}


};
int qmult(int q1_in, int q2_in){  //1 i(2) j(3) k(4)
	int q1=abs(q1_in);
	int q2=abs(q2_in);
	int out=0;

	if(q1==1) out=q2;

	if(q2==1) out=q1;

	if(q1==q2) out=-1;  //(and not both=1)

	if(q1==2){
		if(q2==3) out= 4;
		if(q2==4) out= -3;

	}
	if(q1==3){
		if(q2==4)  out=  2;
		if(q2==2)  out= -4;

	}
	if(q1==4){
		if(q2==2)  out=  3;
		if(q2==3)  out= -2;
	}
	out*=q1_in*q2_in/(q1*q2);

	return out;



}
int qmult_backwards(int q1_in, int q2_in){  //1 i(2) j(3) k(4)
	if(abs(q1_in)==1||abs(q2_in)==1) {
		return qmult(q1_in, q2_in);
	}else{
		return -1*qmult(q1_in, q2_in);
	}
}

string get_ans(vector<int> v){
	vector<int> kbuf;
	//kbuf.resize(v.size());
	{
		int kb=1;
		
		for(int ik=v.size()-1;ik>1;ik--){
			kb=qmult(v[ik],kb);
			kbuf.push_back(kb);
		}


	}

	int v1,v2,v3;
	v1=1;

		for(int ix=1;ix<v.size()-1;ix++){
			v1=qmult(v1,v[ix-1]);
			if(v1==2){
				v2=1;
				for(int iy=ix+1;iy<v.size();iy++){
					v2=qmult(v2,v[iy-1]);
					
					if(v2==3){
						v3=kbuf[v.size()-1-iy];
						//v3=v[iy];
						//for(int k=iy+1;k<v.size();k++){
						//	v3=qmult(v3,v[k]);
						//}
						if(v3==4) return "YES";
					
					}


				}


			}

		}

		return "NO";
}
string get_ans_old(vector<int> v){
			
	
	int v1,v2,v3;
	v1=v[0];

		for(int ix=1;ix<v.size()-1;ix++){
			v1=qmult(v1,v[ix]);

			for(int iy=ix+1;iy<v.size();iy++){

				if(v1==2){
					v2=v[ix];
					for(int j=ix+1;j<iy;j++){
						v2=qmult(v2,v[j]);
					}
					if(v2==3){
						v3=v[iy];
						for(int k=iy+1;k<v.size();k++){
							v3=qmult(v3,v[k]);
						}
						if(v3==4) return "YES";
					
					}


				}


			}

		}

		return "NO";
}
int qmult_old(int q1, int q2){  //1 i(2) j(3) k(4)
	if(q1==1){return q2;}
	if(q1==-1){return -1*q2;}
	if(q2==1){return q1;}
	if(q2==-1){return -1*q1;}
	if(q1==q2){return -1;}  //(and not both=1)
	if(q1==-1*q2){return 1;}  //(and not both=1)
	if(q1==2){
		if(q2==3) return 4;
		if(q2==4) return -3;
		if(q2==-3) return -4;
		if(q2==-4) return 3;
	}
	if(q1==3){
		if(q2==4)  return 2;
		if(q2==2)  return -4;
		if(q2==-4) return -2;
		if(q2==-2) return 4;
	}
	if(q1==4){
		if(q2==1)  return 2;
		if(q2==3)  return -2;
		if(q2==-1) return -2;
		if(q2==-3) return 2;
	}



}


int main(int argc, char* argv[])
{
	string inputfilename="input.txt";
	string outputfilename="output.txt";
	ifstream infile(inputfilename);
	ofstream OF(outputfilename);
	int T;
	infile>>T;
	

	
	
	
	long int l,x;
	
	
	for(int icase=0;icase<T;icase++){
		cout<<icase<<endl;
		vector<int> v;
			
		string s;

		infile>>l>>x;
		infile>>s;
		if(x>12){x=12+x%4;}

		//cout<<l<<"	"<<x<<endl;
		//cout<<s<<endl;

		for(int ix=0;ix<x;ix++){
			for(int ic=0;ic<l;ic++){
				if(s[ic]=='i') v.push_back(2);
				if(s[ic]=='j') v.push_back(3);
				if(s[ic]=='k') v.push_back(4);
				
			}

		}
		//for(int i=0;i<v.size();i++){
		//	cout<<v[i];
		//}
		//cout<<endl;
		//cout<<get_ans(v)<<endl;

		OF<<"Case #"<<icase+1<<": "<<get_ans(v)<<endl;
	}

	

	infile.close();
	OF.close();
	return 0;
}



