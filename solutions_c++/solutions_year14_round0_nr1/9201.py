#include<stdio.h>
#include<string.h>
#include<iostream>
#include<iostream>
#include<string>
#include<list>
#include<iterator>


using namespace std;
struct arr{

  int mat[4][4]; 
}temp_mat;

//typedef arr1 arr;
int main() {

  int tests,temp_ans,i,j,ans_col_index=-1,count=0,test_count=1;
  std::list<arr> mat1, mat2;
  std::list<int> ans1, ans2;  
  scanf("%d",&tests);


  if(1<=tests<=100){
   test_count=1;
   while(test_count<=tests) {
     scanf("%d",&temp_ans);
     ans1.push_back(temp_ans);
     if(1<=temp_ans<=4){
       
       for(i=0;i<4;i++) {
         for(int j=0;j<4;j++){

            scanf("%d",&temp_mat.mat[i][j]);
         }
       }
      
       mat1.push_back(temp_mat);
       scanf("%d",&temp_ans);
       ans2.push_back(temp_ans);

       if(1<=temp_ans<=4){

         for(i=0;i<4;i++) {
           for(j=0;j<4;j++){

              scanf("%d",&temp_mat.mat[i][j]);
           }
         }
         mat2.push_back(temp_mat);
        }//ans2 condition ends
     }//ans1 condition ends
     test_count++;
   }//while loop ends
 
      test_count=1;
      list<arr>:: iterator imat1=mat1.begin();
      list<arr>:: iterator imat2=mat2.begin();
      list<int>:: iterator ians1=ans1.begin();
      list<int>:: iterator ians2=ans2.begin();
      while(test_count<=tests){
         
         //cross check with mat2
         ans_col_index=-1;
         count=0;
         for(i=0;i<4;i++) {
     
           for(j=0;j<4;j++){
              if((*imat2).mat[*ians2-1][i]==(*imat1).mat[*ians1-1][j]){
                 count++;
                 ans_col_index=i;
              }
           }
         }

         if(count==1){
    
            cout<<"\nCase #"<<test_count<<": "<<(*imat2).mat[*ians2-1][ans_col_index];
         }
         else if(count>1) {
 
            cout<<"\nCase #"<<test_count<<": Bad magician!";

         }
         else {
            cout<<"\nCase #"<<test_count<<": Volunteer cheated!";
         }

      test_count++;
      imat1++;
      imat2++;
      ians1++;
      ians2++;
    }//while loop ends
  }//if test_no condition ends  

  else {

      cout<< "large no of tests";

  }
  return 0;
  
}
