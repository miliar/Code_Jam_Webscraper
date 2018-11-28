#include <iostream>
#include <fstream>
#include <string>

using namespace std;
bool flag[2000];

int main() {
    ifstream infile("A-large.in");
    ofstream outfile("A-large.out");

    //outfile<<"case #"<<it<<": INSOMNIA"<<endl;
    int N, counter;
    int nums[10] = {0};
    string str,result;
    infile>>N;
    for(int it=1;it<=N;it++){
        for(int i=0;i<10;i++) nums[i] = 0;
        infile>>str;
        while(str.length()>0){
            if(str.find('Z')<str.length()){
                str = str.replace(str.find('Z'),1,"");
                str = str.replace(str.find('E'),1,"");
                str = str.replace(str.find('R'),1,"");
                str = str.replace(str.find('O'),1,"");
                nums[0]++;
                continue;
            }
            else if(str.find('W')<str.length()){
                str = str.replace(str.find('T'),1,"");
                str = str.replace(str.find('W'),1,"");
                str = str.replace(str.find('O'),1,"");
                nums[2]++;
                continue;
            }
            else if(str.find('U')<str.length()){
                str = str.replace(str.find('F'),1,"");
                str = str.replace(str.find('O'),1,"");
                str = str.replace(str.find('U'),1,"");
                str = str.replace(str.find('R'),1,"");
                nums[4]++;
                continue;
            }
            else if(str.find('X')<str.length()){
                str = str.replace(str.find('S'),1,"");
                str = str.replace(str.find('I'),1,"");
                str = str.replace(str.find('X'),1,"");
                nums[6]++;
                continue;
            }
            else if(str.find('G')<str.length()){
                str = str.replace(str.find('E'),1,"");
                str = str.replace(str.find('I'),1,"");
                str = str.replace(str.find('G'),1,"");
                str = str.replace(str.find('H'),1,"");
                str = str.replace(str.find('T'),1,"");
                nums[8]++;
                continue;
            }
            else if(str.find('T')<str.length()){
                str = str.replace(str.find('T'),1,"");
                str = str.replace(str.find('H'),1,"");
                str = str.replace(str.find('R'),1,"");
                str = str.replace(str.find('E'),1,"");
                str = str.replace(str.find('E'),1,"");
                nums[3]++;
                continue;
            }
            else if(str.find('S')<str.length()){
                str = str.replace(str.find('S'),1,"");
                str = str.replace(str.find('E'),1,"");
                str = str.replace(str.find('V'),1,"");
                str = str.replace(str.find('E'),1,"");
                str = str.replace(str.find('N'),1,"");
                nums[7]++;
                continue;
            }
            else if(str.find('O')<str.length()){
                str = str.replace(str.find('O'),1,"");
                str = str.replace(str.find('N'),1,"");
                str = str.replace(str.find('E'),1,"");
                nums[1]++;
                continue;
            }
            else if(str.find('V')<str.length()){
                str = str.replace(str.find('F'),1,"");
                str = str.replace(str.find('I'),1,"");
                str = str.replace(str.find('V'),1,"");
                str = str.replace(str.find('E'),1,"");
                nums[5]++;
                continue;
            }
            else if(str.find('N')<str.length()){
                str = str.replace(str.find('N'),1,"");
                str = str.replace(str.find('I'),1,"");
                str = str.replace(str.find('N'),1,"");
                str = str.replace(str.find('E'),1,"");
                nums[9]++;
            }
        }
        result = "";
        for(int i=0;i<10;i++){
            for(int j=0;j<nums[i];j++){
                result += (char)(i+'0');
            }
        }

        outfile<<"case #"<<it<<": "<<result<<endl;
    }

    infile.close();
    outfile.close();

    return 0;
}
