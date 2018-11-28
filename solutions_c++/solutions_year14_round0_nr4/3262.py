/*Find the greatest product of five consecutive digits in the 1000-digit number.*/
#include<algorithm>
#include<iostream>
#include<fstream>
#include<iomanip>
#include<math.h>
#include<string>
#include<vector>
using namespace std;


int main(int argc, char** argv){
  
char file1[100]; sprintf(file1, "output_3rd.txt");     ofstream parOP(file1);
int line=0;
int case_number=0;
int i=0;
int j=0;
int z=0;
int flag=0;
int N=0;
int * two_space=new int[1000];
int * three_points=new int[1000];

double * Naomi = new double[1000];
double *  Ken  = new double[1000];
vector<double> Ken_arranged;  
vector<double> Ken_arranged2;  
vector<double> Naomi_arranged;
double Max_Ken=0.0;
double Min_Ken=1.0;
int score_Naomi_war=0;
int score_Naomi_deceitful_war=0;

 ifstream myReadFile;
 myReadFile.open("D-large.in");
 string output;
  //cout<<"go"<<endl;
  if (myReadFile.is_open()) {
    while (!myReadFile.eof()) { 
     getline(myReadFile,output);
      line=line+1;
  //cout<<"line"<<line<<endl;
  //cout<<output.size()<<" size "<<endl;;
     if(line>=2&&(output.size()<=4&&output.size()>=1)){N=0;score_Naomi_war=0;
       for(i=0;i<output.size();i++){
       N+=pow(10,output.size()-i-1)*(int)(output[i]-'0');
    //   cout<<" pow(10,output.size()-i-1)*(int)(output[0]-'0') "<<(int)(output[i]-'0')<<endl;
      }
        line=2;
     }
     
      if(line==3&&output.size()>0){  case_number+=1;i=0;z=0;
        for(j=0;j<output.size();j++){
         if((int)(output[j]-'0')<-2){two_space[i]=j;i=i+1;}
         if((int)(output[j]-'0')==-2){three_points[z]=j;z=z+1;}        
	}
       two_space[N-1]=output.size();
        for(j=0;j<N;j++){Naomi[j]=0;
         for(i=three_points[j]+1;i<two_space[j];i++){
	   Naomi[j]=Naomi[j]+pow(0.1,i-three_points[j])*(int)(output[i]-'0');
          }
         }
      }// end for line=3  
      //cout<<endl;
      
      if(line==4&&output.size()>0){Max_Ken=0.0; Min_Ken=1.0;
        for(j=0;j<N;j++){Ken[j]=0;
         for(i=three_points[j]+1;i<two_space[j];i++){
	  Ken[j]=Ken[j]+pow(0.1,i-three_points[j])*(int)(output[i]-'0');
          } 
         }
	
	sort(Ken,Ken+N);sort(Naomi,Naomi+N);
	//cout<<endl;
	Ken_arranged2.clear();Naomi_arranged.clear();Ken_arranged.clear();
	for(j=0;j<N;j++){Ken_arranged.push_back(Ken[j]);
	Ken_arranged2.push_back(Ken[j]);
	Naomi_arranged.push_back(Naomi[j]);
	//cout<<Ken[j]<<" original ";
       // cout<<Naomi_arranged[j]<<" Naomi "<<endl;
	//cout<<Ken_arranged2[j]<<" vector "<<endl;
	}

//####################calculate the point for war
score_Naomi_war=0;
       for(j=0;j<N;j++){
        if(Naomi[j]>Ken_arranged[Ken_arranged.size()-1]){
	  score_Naomi_war+=1;
	 Ken_arranged.erase(Ken_arranged.begin()+0);//Ken deletes the smallest
         }
        if(Naomi[j]<Ken_arranged[0]){
	 Ken_arranged.erase(Ken_arranged.begin()+0);//Ken deletes the smallest
	}
	if(Naomi[j]>=Ken_arranged[0]&&Naomi[j]<=Ken_arranged[Ken_arranged.size()-1]){
          for (i=0;i<Ken_arranged.size();i++){if(Ken_arranged[i]>Naomi[j])break;}
           Ken_arranged.erase(Ken_arranged.begin()+i);//Ken deletes the smallest who is bigger than Naomi
	} 
      }
//####################calculate the point for war

//####################calculate the point for the deceitful war
score_Naomi_deceitful_war=0;
while(Ken_arranged2.size()>=1){
  //cout<<Ken_arranged2.size()<<endl;
  if(Ken_arranged2.size()==1){
    if(Naomi_arranged[Naomi_arranged.size()-1]>Ken_arranged2[Ken_arranged2.size()-1])
    { //cout<<Naomi_arranged[Naomi_arranged.size()-1]<<Ken_arranged2[Ken_arranged2.size()-1]<<endl;
     score_Naomi_deceitful_war+=1;}//cout<<" Here"<<score_Naomi_deceitful_war<<endl;}
     Ken_arranged2.erase(Ken_arranged2.begin()+0);
  }
/*  
   if((Ken_arranged2.size()>1)&&(Naomi_arranged[0]<Ken_arranged2[Ken_arranged2.size()-1])){
      Ken_arranged2.erase(Ken_arranged2.begin()+Ken_arranged2.size()-1);
      Naomi_arranged.erase(Naomi_arranged.begin()+0);
   }
  
    if((Ken_arranged2.size()>1)&&(Naomi_arranged[0]s>Ken_arranged2[Ken_arranged2.size()-1])){
         Ken_arranged2.erase(Ken_arranged2.begin()+0);
       Naomi_arranged.erase(Naomi_arranged.begin()+0);
 
      score_Naomi_deceitful_war+=1; cout<<" Nein, Hier "<<score_Naomi_deceitful_war<<endl;
   }
*/
   if((Ken_arranged2.size()>1)&&(Naomi_arranged[0]<Ken_arranged2[0])){
      Ken_arranged2.erase(Ken_arranged2.begin()+Ken_arranged2.size()-1);
      Naomi_arranged.erase(Naomi_arranged.begin()+0);
   }
   
   if((Ken_arranged2.size()>1)&&(Naomi_arranged[0]>Ken_arranged2[0])){
         Ken_arranged2.erase(Ken_arranged2.begin()+0);
       Naomi_arranged.erase(Naomi_arranged.begin()+0);
 
      score_Naomi_deceitful_war+=1; //cout<<" Nein, Hier "<<score_Naomi_deceitful_war<<endl;
   }
}
      parOP<<"Case #"<<case_number<<": "<<" "<<score_Naomi_deceitful_war<<" "<<score_Naomi_war<<endl;
      
      }//end line 4      
    }
        myReadFile.close();
  }  

  
parOP.close();

delete two_space;
delete three_points;
delete Ken;
delete Naomi;
  return 0;
}



