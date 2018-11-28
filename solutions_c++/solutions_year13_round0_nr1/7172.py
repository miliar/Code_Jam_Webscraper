#include<iostream>
#include<fstream>
#include<string>
#include<stdlib.h>
        using namespace std;

struct vector{
        bool tExists;
bool blankExists;
int sum;

}rowArr[4],colArr[4],diagArr[2],*diagArrPtr;
ofstream opFile;


bool drawFlag;
string status;
string xOwnString="X won";
string oOwnString="O won";
string draw="Draw";
string not_finished="Game has not completed";

void processItem(struct vector*item){


        if(item->tExists ==true && abs(item->sum)==3){

        status= item->sum==3?xOwnString:oOwnString;

drawFlag=false;
return;

}
        else if(item->tExists ==false && abs(item->sum)==4){

        status= item->sum==4?xOwnString:oOwnString;
drawFlag=false;
return;
}//else end

        if(item->blankExists==true){
        drawFlag=false;
}
        }    //end function

        void initialize(){
        for(int i=0;i<4;i++){
        rowArr[i].tExists=rowArr[i].blankExists=colArr[i].tExists=colArr[i].blankExists=false;
rowArr[i].sum=colArr[i].sum=0;

}
        for(int i=0;i<2;i++){
        diagArr[i].tExists=false;
diagArr[i].blankExists=false;
diagArr[i].tExists=false;
diagArr[i].blankExists=false;
diagArr[i].sum=0;
diagArr[i].sum=0;

}
        diagArrPtr=NULL;

}


        int main(){


        opFile.open("progout.txt");





string line;int numCases;

ifstream ipFile;
ipFile.open("C:\\Dev-Cpp\\bin\\codejam\\A-large.in");
//(0): A-very-small.in    //(1): A-small-practice.in    //(2): A-large-practice.in
if(!ipFile.is_open()){
        opFile<<"ERROR: invalid file"<<endl;
opFile.close();
return(-1);
}


        getline(ipFile,line);
numCases=atoi(line.c_str());

for(int c=0;c<numCases;c++){

        status="bb";;
drawFlag=true;

initialize();


for(int rowNum=0;rowNum<4;rowNum++){
        getline(ipFile,line);
if (line.empty()) {
        getline(ipFile,line);
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
        rowArr[rowNum].tExists=true;
colArr[col].tExists=true;

if(diagArrPtr!=NULL){
        diagArrPtr->tExists=true;

}
        }
        else{ //when .
        rowArr[rowNum].blankExists=true;
colArr[col].blankExists=true;
if(diagArrPtr!=NULL){
        diagArrPtr->blankExists=true;

}
        }

        }//end for col
        }//end for rownum

        for(int i=0;i<4;i++){
        processItem(&rowArr[i]);
processItem(&colArr[i]);
}
        processItem(&diagArr[0]);
processItem(&diagArr[1]);

if(status.compare(xOwnString)!=0 && status.compare(oOwnString)!=0 ){

        status= drawFlag==true?draw:not_finished;
}


        opFile<<"Case #"<<(c+1)<<": "<<status<<endl;


} //end for each test case

        return 0;
opFile.close();
} //end main











