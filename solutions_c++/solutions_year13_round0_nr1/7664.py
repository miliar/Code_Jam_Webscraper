#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;


int main(){

    int tot_cases;
    int case_num=0;
    int row_num=0;
    string line;
    string outcome;
    vector <vector <string> > grid;

    // get all values in vector grid
    ifstream inp_file("A-large.in");
    if (inp_file.is_open()){

            getline (inp_file,line);
            istringstream iss(line);
            iss >> tot_cases;

            grid.resize(tot_cases,vector<string>(4,"...."));

            // enter rows for grid
             while (inp_file.good() )
                      {
                         getline(inp_file,line);
                         cout << line << "\n";
                         grid[case_num][row_num++] = line;

                         if(row_num   == 4 && inp_file.good() ) //processing after last row
                         {
                             row_num=0;
                             case_num++;
                             getline(inp_file,line);
                             cout << "\n";
                         }

                      }
     inp_file.close();
    }

   cout << grid.size();
  ofstream myfile ("solution.txt");
   int incr;

   cout << grid.size();
    for(int t=0; t < grid.size();t++){ // once for each case
            vector <int> vals(10,0);
            int dots =0;
             for(int r=0;r < 4; r++){  // once for each row
                    for(int c=0;c < 4; c++){ //once for each char in the row

                        if(grid[t][r][c] == 'X') incr = 1;
                        if(grid[t][r][c] == 'O') incr = -1;
                        if(grid[t][r][c] == 'T') incr = 15;
                        if(grid[t][r][c] == '.') {incr = 0; dots++; }

                        //cout << grid[t][r][c];

                        vals[r+1] +=incr; vals[4+c+1] +=incr;
                        if(r==c) vals[0] +=incr;
                        if(r+c == 3) vals[9] +=incr;
                    }

                }

       // print the outcome
        for(int v=0;v<10; v++){

                cout << vals[v] << " " << dots << " \n";
        if(vals[v]==  4  || vals[v]== 18) {myfile <<"Case #"<< t+1 <<": X won" <<"\n"; break;}
        if(vals[v]== -4  || vals[v]== 12 ) { myfile <<"Case #"<< t+1 <<": O won" <<"\n"; break;}
        if( v==9){
        if(dots==0) { myfile <<"Case #"<< t+1 <<": Draw" <<"\n";}
        if(dots >0) {myfile <<"Case #"<< t+1 <<": Game has not completed" <<"\n";}
        }
       }
       cout << "\n \n";
           }






        myfile.close();

return 0;
}
