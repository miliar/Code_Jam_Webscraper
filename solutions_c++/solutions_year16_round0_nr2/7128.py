//Design By Robert Jiun-Ting Jiang 20160409
//gcj2016_qualify_pb__½½stack 
//Dev-C++
#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>

//#include <fstream>

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

int FStack[100+1]; //��J+���1�A-���0 
int n_FStack=0;
//ifstream fin("in.txt"); 


//�g�@��½½Stack����� �ѳ̥��Ĥ@�� ����w����n��½�@��

int  flipFStack(int n) { 
	//0����1,  
	int t;		
	/*if (n%2 != 0) { 
		//FStack[n/2+1] = ZeroOneSwap(FStack[n/2+1]); //^1;
		FStack[n/2+1]^1;
	}
	for (int i=1 ; i<=n/2;i++){
		//t=ZeroOneSwap(FStack[i] ); FStack[i]=ZeroOneSwap(FStack[n-i+1]);  FStack[n-i+1]=t;
		t=FStack[i]^1; FStack[i]=FStack[n-i+1]^1;  FStack[n-i+1]=t;}
	*/
	for (int i=1 ; i<=n;i++){
		FStack[i]^=1;
	}
	for (int i=1 ; i<=n/2;i++){		
		t=FStack[i]; FStack[i]=FStack[n-i+1];  FStack[n-i+1]=t;
	}	
	return 0;
}

int main() {
  
    int n_testcase, i, j, x, y;

    cin >> n_testcase;    
    for ( int i_testcase=1; i_testcase<=n_testcase;i_testcase++)  {        
        cout << "Case #" << (i_testcase) << ": ";
		string ss_in;
        cin >> ss_in;

        int ii;
        for (int i=1;i<=ss_in.length(); i++){
			FStack[i]=(ss_in.substr(i-1,1)=="-"?0:1);
			ii=i;
		}
		//FStack[ii+1]=999;
		//�����|���G�p�G�ݳB�z�ϰ쬰1..i �h 
		//case  0 0,  0 1,  1 0,   1,1
		
		//�Y������1��ܤw���T�C�N�� 1..i�אּ 1..(i-1)
		//�Y��������1���0, �n�Ѳ�1�ӨӴ��A�Y
		//              �Y ��1�ӭ�n�O0�A�h½�L�ӫ�A�N�⥼���ܬ�1�A
		//              �Y ��1�ӫo�O1�A�h�n�ѧ��� (i-1) ..(1)�˵ۧ�A���즳1�A�⨺��1½��̫e��0�A�~�i�H�A½�쥼���ܬ�1
		
					
		n_FStack=0;
		//�ѥ����ˬd �A�ݬO�_�n½Stack�åB�O���`�@½�X���C 
		for (int i=ss_in.length();i>=1; i--){
			if (FStack[i]==1) {
			} else { //0�h�n���ݫe���O0,1? 
			    //�{�b������ [i]�O0�A�ҥH�n½�I 
				if (FStack[1]==0){
					n_FStack++;
					flipFStack(i) ;
				} else {
					//�n������1���ܬ�0�A�ҥH�ѥ���(i-1)���e��Ĥ@��1.
					int iTail=i-1;
					for (;iTail>=1; iTail--){
						if(FStack[iTail]==1)break; //�̦h�N���Ĥ@�Ӫ�1 
					}
					n_FStack++;
					flipFStack(iTail);
					//���ɲĤ@���ܬ�0�F�A�ҥH�i�H����½�A�ϥ�����1 
					flipFStack(i) ;
					n_FStack++;
				}
			}
		}
        cout << n_FStack << endl;
    }
    return 0;
}


