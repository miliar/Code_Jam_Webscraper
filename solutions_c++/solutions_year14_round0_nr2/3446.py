/*Find the greatest product of five consecutive digits in the 1000-digit number.*/

#include<iostream>
#include<fstream>
#include<iomanip>
#include<math.h>
#include<string>

using namespace std;

bool decision(double C, double F, double X, int farm_number){
  int decis=0;
double   product_rate=0.0;//2.0+farm_number*F;
double   potential_product_rate=0.0;//2.0+(1+farm_number)*F;
double   t_to_build_a_farm_to_X=0.0;//(C)/product_rate+X/potential_product_rate;
double   t_to_atteint_X=0;//(X)/product_rate;

  product_rate=2.0+farm_number*F;
   potential_product_rate=2.0+(1+farm_number)*F;
   t_to_build_a_farm_to_X=(C)/product_rate+X/potential_product_rate;
   t_to_atteint_X=(X)/product_rate;
// cout<<" product_rate "<<product_rate<<" potential_product_rate "<<potential_product_rate<<endl;
// cout<<" t_to_build_a_farm_to_X "<<t_to_build_a_farm_to_X<<" t_to_atteint_X "<<t_to_atteint_X<<endl;
  if(t_to_build_a_farm_to_X>t_to_atteint_X)
     {decis=0;}//Just wait
  
  if(t_to_build_a_farm_to_X<=t_to_atteint_X)
    {decis=1;}// To build a farm
   // cout<<decis<<" make the decision"<<endl;
  return decis; // decis=1, build a farm; decis=0, wait.
}

int main(int argc, char** argv){
  
char file1[100]; sprintf(file1, "output_2nd.txt");     ofstream parOP(file1);

double C=0.0;
double F=0.0;
double X=0.0; //winning value
int farm_number=0;
double product_rate=2.0+farm_number*F;
double potential_product_rate=2.0+(1+farm_number)*F;
double sum=0.0;
double t_to_build_a_farm_to_X=0.0;
double t_to_atteint_X=0.0;
double total_t=0.0;






int line=0;
int case_number=0;
int i=0;
int j=0;
int z=0;
int flag=0;
int * two_space=new int[2];
int * three_points=new int[3];

 ifstream myReadFile;
 myReadFile.open("B-large.in");
 string output;
  
  if (myReadFile.is_open()) {
    while (!myReadFile.eof()) { 
     getline(myReadFile,output);
     C=0.0; F=0.0;X=0.0;
      line=line+1;
      //cout<<line<<endl;
  //   cout<<output.size()<<endl;
   
//      if(line==2){first_row=0;first_row=(int)(output[0]-'0');}
   
      if(line>=2&&output.size()>0){  case_number+=1;i=0;z=0;
        for(j=0;j<output.size();j++){
         if((int)(output[j]-'0')<-2){two_space[i]=j;i=i+1;}
         if((int)(output[j]-'0')==-2){three_points[z]=j;z=z+1;}        
	}
      

      for(i=0;i<three_points[0];i++){C=C+pow(10,three_points[0]-1-i)*(int)(output[i]-'0');}
      for(i=three_points[0]+1;i<two_space[0];i++){C=C+pow(0.1,i-three_points[0])*(int)(output[i]-'0');}
      cout<<fixed;
      //cout<<setprecision(11)<<C<< " C ";

      for(i=two_space[0]+1;i<three_points[1];i++){F=F+pow(10,three_points[1]-1-i)*(int)(output[i]-'0');}
       for(i=three_points[1]+1;i<two_space[1];i++){F=F+pow(0.1,i-three_points[1])*(int)(output[i]-'0');}
      //cout<<F<< " F ";

      for(i=two_space[1]+1;i<three_points[2];i++){X=X+pow(10,three_points[2]-1-i)*(int)(output[i]-'0');}             for(i=three_points[2]+1;i<output.size();i++){X=X+pow(0.1,i-three_points[2])*(int)(output[i]-'0');}
      //cout<<X<< " x "<<endl;

       total_t=0;farm_number=0;product_rate=2.0+farm_number*F;
    
       flag=decision(C, F, X, farm_number);   
      //cout<<flag<<" first decision"<<endl;
       
      while(flag==1){        
	total_t+=(C)/(2.0+farm_number*F);
        farm_number+=1;
        product_rate=2.0+farm_number*F;
       flag=decision(C, F, X, farm_number);
      // cout<<flag<<endl;
}

     if(flag==0){total_t+=X/(product_rate);}
//       cout<<fixed;
//       cout<<"Case #"<<case_number<<": "<<setprecision(7)<<total_t<<endl; //outputtheresult 
        parOP<<fixed;
       parOP<<"Case #"<<case_number<<": "<<setprecision(7)<<total_t<<endl; //outputtheresult 

	
      }  
     }
        myReadFile.close();
  }  

parOP.close();
  return 0;
}



