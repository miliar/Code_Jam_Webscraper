#include <QCoreApplication>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>

using namespace std;


int main(int argc, char *argv[])
{
    //QCoreApplication a(argc, argv);
    //return a.exec();
    ifstream myreadfile;
    fstream file;
    string str;
    int t_count;
    int shyMax;
    int size,space_pos;
    string t_string;
    char temp[1];
    u_int16_t count,friends;

    myreadfile.open("/home/nima/opera/input.txt");
    file.open("/home/nima/opera/output.in");


    if(myreadfile.is_open()){
        //printf("YES\n")  ;
    }
    else{

    printf("File Load Fail\n");    }
    getline(myreadfile,str);
    t_count=std::atoi(str.c_str());

    for(int i=0;i<t_count;i++){
        count=0;
        friends=0;
        getline(myreadfile,t_string);
        space_pos = t_string.find(" " , 0);
        shyMax=std::atoi(t_string.substr(0,space_pos).c_str());
        t_string=t_string.substr(space_pos+1,size).c_str();
        //cout<< "shy="<<shyMax<<endl;
        //cout<<t_string+"\n";
        for(int j=0;j<=shyMax;j++){
            temp[1]=t_string.at(j);
            int temp_num=(int)(temp[1]-'0');
            if(temp_num>0){

                if (count<j) {
                    friends+=j-count;
                    count=count+(j-count)+temp_num;
                    //cout<<friends;
                } else {
                    count=count+temp_num;

                }
          }



        }

        file << "Case #"<<i+1<<":"<<' '<<friends<<endl;
        //file.close();
        cout<<"case #"<<i<<":"<<friends<<endl;
    }


    while (getline(myreadfile,str)) {
        //cout<<str+"\n";
     }

}
