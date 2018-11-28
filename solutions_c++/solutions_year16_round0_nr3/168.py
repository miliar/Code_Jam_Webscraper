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
#include <time.h>

using namespace std;

int N;
int J;

const int L=5000;
int C[L+1];

void MAKE_PRIME_TABLE(void);

vector<int>PRIME;

int D[33];

void MAKE_RANDOM_NUM(void);

int CHECK(void);

set<string> S; //���ׂ����̂��i�[���Ă���

int DEVISION(int base); // C[]�Ɋi�[���ꂽ���base�ň����������A�쐬�����L���̑f���Ŋ���邩�ǂ����𔻒�
                        // �����Ί���鐔��Ԃ��A�L���̑f���\�͈͓̔��Ŋ���Ȃ����-1��Ԃ�

vector<int> ans;
int main()
{
	ifstream ifs("C-large (1).in");
    ofstream ofs("answer_C_large");

	MAKE_PRIME_TABLE();

	/*for(int i=0;i<int(PRIME.size());i++){
      cout<<PRIME[i]<<" ";
	}*/


     srand((unsigned)time(NULL));

	int T;
	ifs >> T; cout << "T= " << T <<endl;
   
   for(int t=0;t<T;t++){  // test cases

    ifs >> N; cout << "N= " << N << endl; 
    
    ifs >> J; cout << "J= " << J << endl;

    cout << "Case #" <<t+1<<": " <<endl;
    ofs << "Case #" <<t+1<<": " <<endl;

	int Num_D;

	int j=0;
	while(j<J){
       MAKE_RANDOM_NUM();  //��������
	   for(int k=0;k<N;k++){cout<< C[k];} cout<<"   "; // �����̕\��

	   if(CHECK()==-1){cout<< "continue"<<endl; continue;} //�ȑO�ɒ��ׂ����̂͏��O

       ans.clear();

	   for(int base=2; base<=10;base++){
		   Num_D=DEVISION(base);
		   if(Num_D==-1){cout<<"No "<<endl; break;}
		   else{ ans.push_back(Num_D); }
	   }// for fin

	   if(Num_D!=-1){
		   //---------------------------
		   cout << "Yes ";
	   for(int n=0;n<int(ans.size());n++){
            cout << ans[n]<<" ";
	   }
	   cout<<endl;
           //----------------------------
	   for(int m=0;m<N;m++){
         ofs<<C[m];
	   }
	   for(int m=0;m<int(ans.size());m++){
        ofs<<" " << ans[m];
	   }
	   ofs<<endl;
	   j++;
	                } // Num_D!=-1�̂Ƃ��̏o��

	}// ����������while���[�v�I��



   } // end of test cases

 return 0;
}

void MAKE_PRIME_TABLE(void)
{
	for(int i=1;i<=L;i++){
       C[i]=1;
	}
 
	for(int I=2;I<=L;I++){
		if(C[I]==1){
			for(int j=2;;j++){
				if(j*I>L){break;}
				else{C[j*I]=0;  }
			}
		}
	}

	for(int i=2;i<=L;i++){
		if(C[i]==1){PRIME.push_back(i);}
	}
}

void MAKE_RANDOM_NUM(void)
{
     C[0]=1;

	 unsigned u;
	 for(int i=1;i<=N-2;i++){
       u=rand()%2;
	   C[i]=u;
	 }

	 C[N-1]=1;
}

int CHECK(void)
{
  string str;

  for(int i=0;i<N;i++){
	  if(C[i]==1){str+="1";}
	  else{str+="0";}
  }

  if(S.find(str)==S.end()){ //�v�f��������Ȃ��ꍇ
        S.insert(str); return 1;
  }else{ //�v�f�����������ꍇ
     return -1;
  }

}


int DEVISION(int base)
{
 long long K;

 int j=0;
 while(j<int(PRIME.size())){
 K=C[0];
 for(int i=1;i<=N-1;i++){
 K=(K*base+C[i])%PRIME[j];
 }
 if(K==0){return PRIME[j];}
 j++;
 }
 return -1;
}