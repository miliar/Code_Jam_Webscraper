#include<iostream>
#include <limits>
#include<fstream>
#include<iomanip> 
#include <vector>
using namespace std;

int main(){
    int t;   
    int caseseq[t];//1 succeed 0 Volunteer cheated!(no)  -1 Bad magician!(mul)
    long long a1[4];
    long long a2[4];
    int tem;
    
    fstream fin;
    fin.open("D:\\in.txt");
     
    fin>>t;
    for(int i=0;i<t;i++){
        vector<int> result;
      fin >> caseseq[i];
      cout<<"case "<<caseseq[i]<<endl;
      
      for(int j=0;j<caseseq[i];j++){
          for(int k=0 ; k<4 ;k++)
                fin>>a1[k]; 
      }
      for(int j=0;j<4-caseseq[i];j++)
          for(int k=0 ; k<4 ;k++)
              fin>>tem;
      
      fin >> caseseq[i];
      cout<<caseseq[i]<<endl;
      for(int j=0;j<caseseq[i];j++){
          for(int k=0 ; k<4 ;k++)
                fin>>a2[k]; 
      }
      for(int j=0;j<4-caseseq[i];j++)
          for(int k=0 ; k<4 ;k++)
              fin>>tem;

      for(int j=0; j<4;j++){
          cout << a1[j]<<" ";
      }
      cout<<endl;
      for(int j=0; j<4;j++){;
          cout << a2[j]<<" "; 
      }
      cout<<endl;

      for(int k=0 ; k<4 ;k++)
          for(int j=0 ; j<4 ;j++){
              if(a1[j]==a2[k]){
                  result.push_back(a2[k]);

              }
          } 
      
      if(result.size()==1)
          caseseq[i]=result[0];
      if(result.size()==0)
          caseseq[i]=0;
      if(result.size()>1)
          caseseq[i]=-1;

    }
     fin.close();

    fstream fout;
    fout.open("D:\\Users\\Ebrai\\Documents\\NetBeansProjects\\Problem A. Minimum Scalar Product\\out.txt", ios::out);
    for( int i=0;i<t;i++){
    	
        fout << "Case #"<<i+1 << ": ";
        if(caseseq[i]>0)
			fout<<std::fixed<< caseseq[i]<<"\r\n";
		if(caseseq[i]==0)
			fout<<"Volunteer cheated!"<<"\r\n";
		if(caseseq[i]==-1)
			fout<<"Bad magician!"<<"\r\n";
        
    }
    fout.close();
    
  return 0;
}
