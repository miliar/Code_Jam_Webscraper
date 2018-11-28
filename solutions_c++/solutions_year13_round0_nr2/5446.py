#include <string>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
  FILE *fp;
  errno_t err;
  if((err=fopen_s(&fp,"B-small-attempt1.in","r"))!=0)
  { printf("入力ファイルが開けません\n");
    return -1;
  }

  ofstream ofs("B-small-answer");

  char line[1024];
  fgets(line,sizeof(line),fp);

  int T;
  sscanf_s(line, "%d",&T);

  int N,M;
  int A[10][10];
  for(int t=0;t<T;t++){ // T-loop
    /*-------- N, M ----------------*/
	 fscanf(fp, "%d %d", &N, &M);
	/*------------------------------*/
    /*-------- A -------------------*/
	 for(int i=0; i<N; i++){
		 for(int j=0; j<M; j++){
	  int v;
      fscanf(fp,"%d", &v);
	  A[i][j]=v;
		 }    
	 }
	 /*-----------------------------*/
	 int possible=1;
	 int R=0,C=0;

	 for(int i=0;i<N;i++){
		 for(int j=0;j<M;j++){
			 if(A[i][j]==1){ R=1;C=1;
			 for(int k=0 ;k<N;k++){ if(A[k][j]>1)R=0;}
			 for(int l=0 ;l<M; l++){ if(A[i][l]>1)C=0;}
			 if(R==0 && C==0){possible=0;}
			                }			   
		 }
	 }

result:
	 if(possible==1){ofs << "Case #" << t+1 << ": " << "YES" <<endl;}
	 else{ofs << "Case #" << t+1 << ": " << "NO" <<endl;}

  } // T-loop fin



return 0;
}