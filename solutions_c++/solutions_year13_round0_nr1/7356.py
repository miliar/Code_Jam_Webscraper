#include <iostream>
using namespace std;

int main(int argc, char* argv[]){


  int count;
  cin >> count;
  int empty=0;
  string answersofx[5]={"XXXX","XXXT","XXTX","XTXX","TXXX"};
  string answersofo[5]={"OOOO","OOOT","OOTO","OTOO","TOOO"};
  bool found = false;
  bool found2 = false;
  string lines[4];
  string garbage;

  for(int i=0;i<count;i++){
    
    for(int k=0;k<4;k++)
      cin >> lines[k];
    string diagonal;
    string diagonal2;
    diagonal +=lines[0].at(0);diagonal+=lines[1].at(1);diagonal+=lines[2].at(2);diagonal+=lines[3].at(3);
    diagonal2 +=lines[0].at(3);diagonal2+=lines[1].at(2);diagonal2+=lines[2].at(1);diagonal2+=lines[3].at(0);

    //cout << lines[0]<< endl<<lines[1]<<endl<<lines[2]<<endl<<lines[3]<<endl;

    //cout << " check diagonals" << endl;
    //check diagonals
    for(int k =0; k<5; k++){
      if(answersofx[k]==diagonal || answersofx[k]==diagonal2){
        //cout << "Case #"<< i+1 << ": X Won" << endl;
        found = true;}

      if(answersofo[k]==diagonal || answersofo[k] == diagonal2){
        //cout << "Case #"<<i+1 <<": O Won"<< endl;
        found2 = true;
      }
    }



    //cout<<"check straights" << endl;
    //check straight lines
    for(int k=0;k<4;k++){
      for(int j=0;j<5;j++){
        if(lines[k]==answersofx[j]){
          //cout << "Case #"<< i+1 << ": X won" << endl;
          found=true;}
          
        

        if(lines[k]==answersofo[j]){
          //cout << "Case #"<< i+1 << ": O won" << endl;
          found2=true;}
          
        


      }


    }


    //cout << "check columns" << endl;
    //check straight lines
    for(int j=0;j<4;j++){
      string tmp = "";
      tmp +=lines[0].at(j);tmp+=lines[1].at(j);tmp+=lines[2].at(j);tmp+=lines[3].at(j);

      for(int k=0;k<5;k++){
        if(tmp==answersofx[k]){
          //cout << "Case #"<< i+1 << ": X won" << endl;
          //cout << tmp << endl;
          found = true;
        }
        if(tmp==answersofo[k]){
          //cout << "Case #"<<i+1 <<": O won" << endl; 
          //cout << tmp << endl;
          found2=true;
        }
      }

    }


    //cout << "check if complete"<< endl;
    //checks if complete
    for(int j=0;j<4;j++){
      for(int k=0;k<4;k++){
        if(lines[j].at(k)=='.')
          empty++;
      }

    }



    if(found && found2){
      cout << "Case #"<<i+1<<": Draw"<< endl;
      found=false;
      found2 = false;
      empty=0;
      continue;

    }

    if(found){
      cout << "Case #"<< i+1 << ": X won" << endl;
      found= false;
      found2 = false;
      empty=0;

      continue;
    }

    if(found2){
      cout << "Case #"<< i+1 << ": O won" << endl;
      found2 = false;
      found = false;empty=0;
      continue;
    }
    if(empty!=0)
      cout << "Case #"<< i+1<< ": Game has not completed" << endl;
    else
      cout << "Case #"<<i+1<<": Draw"<< endl;

    empty =0;


  }


}
