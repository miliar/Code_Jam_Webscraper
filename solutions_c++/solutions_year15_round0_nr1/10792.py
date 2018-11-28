//Standing Ovation.cpp

#include <iostream>
#include <string>
#include <fstream>


using namespace std;

void read(string fileName);
void write(int T, int* ans);
int logic(string input);

int main(){
  read("A-small-attempt0.in");
}

int logic(string input){
  int length = input.length();
  //cout << input << '\n';

  int intINPUT[length -1];
  for (int i = 1; i < length; i++){
    intINPUT[i-1] = input[i] - '0';
  }


  int totalPeople = 0;
  int peopleNeed = 0;
  for (int i = 0; i < length-1; i++){
    int count = intINPUT[i];
    if (count != 0){
      if (totalPeople >= i){
        totalPeople += count;
      }else{
        peopleNeed += i - totalPeople;
  
        totalPeople += peopleNeed + count;
      }
    }
  }

  cout << peopleNeed;

  cout << endl;



  return peopleNeed;
}


void read(string fileName){
 	ifstream fin(fileName);

  if (!fin.is_open()){

  }else{

    int T = 0;
    fin >> T;
    
  
      //cout << "T: " << T << '\n';
  
      string input[T];
  
      for (int i = 0; i < T; i++){
        int sMax = 0;
        fin >> sMax;
        //cout << "sMax: " << sMax << "   ";
  
        getline(fin, input[i]);
        //cout << input[i];
        //cout << '\n';
      }
  
      int ans[T];
  
      for (int i = 0; i < T; i++){
        ans[i] = logic(input[i]);
      }
  
  
      write(T, ans);
  

  }
}

void write(int T, int* ans){

	ofstream myfile("answers.txt");
	if (myfile.is_open())
  {
    for (int i = 0; i < T; i++){      

      myfile << "Case #" << i+1 << ": ";      
      myfile << ans[i] << '\n';  



    }          
    myfile.close();
  }
  	else cout << "Unable to open file";
}