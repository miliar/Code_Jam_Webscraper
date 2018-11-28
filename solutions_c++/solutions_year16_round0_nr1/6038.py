#include <iostream>
#include<fstream>
#include<string>
using namespace std;

int main() {
    //open the files
    string fileName = "A-large.in";
    fstream file;
    file.open(fileName);
    
    string outputFile = "output";
    fstream output;
    output.open(outputFile);
            
    //find number of cases
    string line;
    getline(file, line);
    int cases = stoi(line);

    //declare variables
    bool digit[10];            //array of booleans
    int val;
    int sum;
    int curr;
    
    //iterate through cases
    for(int i=0;i<cases;i++){
        //get input
        getline(file,line);
        val = stoi(line);
        
        //only case of Insomnia
        if(val==0){
            output<<"Case #";
            output<<i+1<<": ";
            output<<"Insomnia\n";
        }
        
        else{
            sum = 0;
            for(int i=0; i<10; i++)
                digit[i] = true;
            //go until we see all the digits
            while(digit[0] || digit[1] || digit[2] || digit[3] || digit[4] ||
                  digit[5] || digit[6] || digit[7] || digit[8] || digit[9]){
                //set up to check the digits
                sum += val;
                curr = sum;
                while(curr!=0){
                    digit[curr%10] = false;
                    curr = curr/10;
                }
            }
            output<<"Case #";
            output<<i+1<<": ";
            output<<sum;
            output<<"\n";
        }
    }
    
    //close the file
    output.close();
    file.close();
    return 0;
}

