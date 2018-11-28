#include<iostream>
#include<fstream>
#include<string>
#include<stdlib.h>
        using namespace std;

struct rowColDiag{
        bool tFlag;
bool blankFlag;
int sum;

}rowArr[4],colArr[4],diagArr[2],*diagArrPtr;//r0,c0,r1,c1,r2,c2,r3,c3.d0,d1
 ofstream myfile;


bool drawFlag;
string status;
string x_own="X won";
string o_own="O won";
string draw="Draw";
string not_finished="Game has not completed";

void calculateWinStatus(struct rowColDiag*item){


        if(item->tFlag ==true && abs(item->sum)==3){

        status= item->sum==3?x_own:o_own;
        
drawFlag=false;
return;

}
        else if(item->tFlag ==false && abs(item->sum)==4){

        status= item->sum==4?x_own:o_own;
drawFlag=false;
return;
}//else end

        if(item->blankFlag==true){
        drawFlag=false;
}
        }    //end function

        void initialize(){
        for(int i=0;i<4;i++){
        rowArr[i].tFlag=rowArr[i].blankFlag=colArr[i].tFlag=colArr[i].blankFlag=false;
rowArr[i].sum=colArr[i].sum=0;

}
        for(int i=0;i<2;i++){
        diagArr[i].tFlag=false;
diagArr[i].blankFlag=false;
diagArr[i].tFlag=false;
diagArr[i].blankFlag=false;
diagArr[i].sum=0;
diagArr[i].sum=0;

}
        diagArrPtr=NULL;

}


        int main(){

       
myfile.open("tictacout.txt");





string line;int numCases;

ifstream inputFile;
inputFile.open("C:\\Dev-Cpp\\bin\\codejam\\A-large.in");
//(0): A-very-small.in    //(1): A-small-practice.in    //(2): A-large-practice.in
if(!inputFile.is_open()){
        myfile<<"ERROR: invalid file"<<endl;
myfile.close();
return(-1);
}


        getline(inputFile,line);
numCases=atoi(line.c_str());

for(int c=0;c<numCases;c++){

       status="bb";;
drawFlag=true;

initialize();


for(int rowNum=0;rowNum<4;rowNum++){
        getline(inputFile,line);
        if (line.empty()) {
                        getline(inputFile,line);   
                          }
const char*eachRow=line.c_str();

for(int col=0;col<4;col++){
        diagArrPtr=NULL;
diagArrPtr=rowNum+col==3?&diagArr[1]:diagArrPtr;
diagArrPtr=rowNum==col?&diagArr[0]:diagArrPtr;
if(eachRow[col]=='X'){
        rowArr[rowNum].sum++;
colArr[col].sum++;
if(diagArrPtr!=NULL){
        diagArrPtr->sum++;
}
        }
        else if(eachRow[col]=='O'){
        rowArr[rowNum].sum--;
colArr[col].sum--;
if(diagArrPtr!=NULL){
        diagArrPtr->sum--;

}
        }
        else if(eachRow[col]=='T'){
        rowArr[rowNum].tFlag=true;
colArr[col].tFlag=true;

if(diagArrPtr!=NULL){
        diagArrPtr->tFlag=true;

}
        }
        else{ //when .
        rowArr[rowNum].blankFlag=true;
colArr[col].blankFlag=true;
if(diagArrPtr!=NULL){
        diagArrPtr->blankFlag=true;

}
        }

        }//end for col
        }//end for rownum

        for(int i=0;i<4;i++){
        calculateWinStatus(&rowArr[i]);
//myfile<<"statusrow: "<<status<<endl;
calculateWinStatus(&colArr[i]);
//myfile<<"statuscol: "<<status<<endl;
}
        calculateWinStatus(&diagArr[0]);
//myfile<<"statusdiag: "<<status<<endl;
calculateWinStatus(&diagArr[1]);
//myfile<<"statusdiag: "<<status<<endl;

if(status.compare(x_own)!=0 && status.compare(o_own)!=0 ){

        status= drawFlag==true?draw:not_finished;
}


        myfile<<"Case #"<<(c+1)<<": "<<status<<endl;


        } //end for each test case

        return 0;
myfile.close();
} //end main











