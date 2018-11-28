#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <sys/timeb.h>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <sys/timeb.h>
#include <math.h>

bool repeat(std::string line){
    if (line.length()==1 || line=="") {
        return true;
    }else{
        if (line.at(0)==line.at(line.length()-1)) {
            line.erase(0,1);
            line.erase(line.length()-1,1);
            return repeat(line);
        }else{
            return false;
        }
    }
}

int c_count(int a,int b){
    int i;
    int count=0;
    for(i=a;i<=b;i++){
        float x=0;
        x=sqrt(float(i));
        //printf("i is %d\n",i);
        if (float(x)-int(x)==0) {
            std::stringstream ss;
            //printf("a is %i\n",int(x));
            ss<<int(x);
            std::stringstream sq;
            sq<<i;
            std::string q=sq.str();
            std::string s=ss.str();
            if (repeat(s) && repeat(q)) {
                count++;
                //printf("i is %d\n",i);
            }
        }
    }
    return count;
}

void word_tokenize(std::string s, std::vector<std::string> *tokens) {
    std::istringstream s_stream(s);
    copy(std::istream_iterator<std::string>(s_stream),
         std::istream_iterator<std::string>(),
         std::back_inserter<std::vector<std::string> >(*tokens));
};

int main(){
    std::ifstream infile;
    std::string sline="";
    infile.open("test.txt");
    FILE *pfile;
    pfile=fopen("myfile.txt","w");
    int line=0;
    int n_case=0;
    while(!infile.eof()){
        getline(infile,sline);
        if (line==0) {
            n_case=atoi(sline.c_str());
        }else{
            std::vector<std::string>lines;
            word_tokenize(sline,&lines);
            int a;
            int b;
            int cc=0;
            for (std::vector<std::string>::iterator it_token=lines.begin();
                 it_token != lines.end();
                 it_token++) {
                std::string &single = *it_token;
                if (cc==0) {
                    a=atoi(single.c_str());
                }else{
                    b=atoi(single.c_str());
                }
                cc++;
            }
            fprintf(pfile,"Case #%i: %i\n",line,c_count(a,b));
        }
        line++;
    }
    fclose(pfile);
    
}