//Design By Robert Jiun-Ting Jiang 20160409
//gcj2016_qualify_pa
//Dev-C++
#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
//#include <deque>


/*�� fin , fout ���ɮ׿�X�J���N �зǿ�X�J 
    #include <fstream>
    ifstream fin("in.txt");   
    ofstream fout("out.txt"); 
	// fin>>i;  fout<<"ddd";
*/
//�ഫ���N�κA����ơA��stringstream�ର�r��A�Ҧp�Ʀr���r��C string(number) 
/*int  ans=987;
string ss = "";
stringstream ssm;
ssm.clear();ssm << ans ; ssm >> ss; 
ss = ss.substr(ss.length()-1,1); //�L�X�̥��ӼƦr 
cout << ss << endl;
exit;
*/
using namespace std;

////////////////////////////////////////////////////////////////////////////////

int digHash[10]; 
int digHashMask(long long n){
	while (n>0){
		long long ddd=n/10;
		int mmm=n%10;
		digHash[mmm]++;
		n=ddd;
	}
}


int main() {
    int n_testcase, i, j, x, y;
	//int digHash[10]; 

    cin >> n_testcase;    
    for ( int i_testcase=1; i_testcase<=n_testcase;i_testcase++)  {        
        cout << "Case #" << (i_testcase) << ": ";
		long long n;
        cin >> n;
        //n = 1692;
        //n=2;
        int n_count=-1;
        for (int i=0;i<=9;i++) digHash[i]=0;
        long long n_grow;
	    if (n==0){
        	cout<<"INSOMNIA"<< endl;
		}else { 
			n_grow=n; //�|���j��n 
			n_count=0;       	    					
			while (true){ //	for (;;){			
				n_count++;
	        	digHashMask(n_grow);	        	
	        	//���]:���O0�N�@�w�|�b������n���o��10�ӥ��X�{�I
				int icheck;  // checkAllSee=1;			
				for (icheck=0;icheck<=9; icheck++){
					if (digHash[icheck]==0) break;
				}					
				if (icheck>9) break;
				n_grow+=n;			
			}
			cout << n_grow << endl;
		}		
    }
    return 0;
}

