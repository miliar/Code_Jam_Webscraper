#include <iostream>
#include<fstream>
#include<string>
#include <vector>
using namespace std;

int main() {
    //open the files
    string fileName = "B-large.in";
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
    vector<bool> pancakes;            //vector of booleans
    bool last;
    bool top;
    int curr;
    int sec;
    int flipcount=0;                      //position of first
    int size;                     //position of second
    //iterate through cases
    for(int i=0;i<cases;i++){
        //get input
        pancakes.clear();
        getline(file,line);
        for(int i=0; i < line.size(); i++){
            if(line[i]=='+')
                pancakes.push_back(true);
            else
                pancakes.push_back(false);
        }

        
        //set up variables
        size = pancakes.size();
        last = pancakes[size-1];
        flipcount=0;
        while(true){
            
           top=pancakes[0];
           last = pancakes[size-1];
           curr=0;
           while(last && size>1){
               size--;
               last=pancakes[size-1];
               
            }
           
           if(0==(size-1)){
                if(!last)
                    flipcount++;
            break;
           }
           //both are faced down just need to flip all    
           if(top==last){
                for(int i=0; i<size; i++)
                    pancakes[i] = !pancakes[i];
                flipcount++;
           }
       
           //top is positive and bottom is negative
            else{
                while(pancakes[curr]==pancakes[curr+1] && curr < (size-1))
                    curr++;
                pancakes.erase(pancakes.begin(),pancakes.begin()+curr+1);
                for(int i=0; i<=curr; i++)
                    pancakes.insert(pancakes.begin(),!top);
                flipcount++;
           }
        }
            //output to file
            output<<"Case #";
            output<<i+1<<": ";
            output<<flipcount<<"\n";
    }
    //close the file
    output.close();
    file.close();
    return 0;
}

