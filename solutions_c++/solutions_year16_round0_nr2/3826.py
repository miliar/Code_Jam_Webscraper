#include <iostream>
#include <fstream>
//#include <queue>
using namespace std;

/*int check(string str){
    int i = 1;
    while(i < str.length() && str[0] == str[i]) i++;
    if(i == str.length()){
        if(str[0] == '+') return 0; //all done
        else return 1; //one flip left
    }
    int temp = i;
    while(i < str.length() && str[temp] == str[i]) i++;
    if(i == str.length()){
        if(str[temp] == '+') return 1; //flip top temp panckages
        else return 2; //flip top temp pancakes, then flip all of them
    }
    return -1; //not done yet
}
int solve(string str){
    queue<pair<string, int>> bfs;
    bfs.push(make_pair(str, 0));
    while(true){
        string cake = bfs.front().first;
        int flips = bfs.front().second;
        bfs.pop();
        int soln = check(cake);
        if(soln >= 0){ //done
            return flips + soln;
        }
        //not done yet
        //flip only the first one - flip all but the last one
        for(int i=1;i<cake.length();i++){
            string temp = cake;
            for(int j=0;j<i;j++){
                temp[j] = (cake[i-1-j] == '+')?'-':'+';
            }
            bfs.push(make_pair(temp, flips+1));
        }
    }
}*/

int solve2(string str){
    if(str == "+") return 0;
    else if(str == "-") return 1;

    int chunks = 0;
    int i = 0,j = 1;
    while(j < str.length()){
        while(j < str.length() && str[i] == str[j]) j++;
        chunks++;
        //now str[j] is first cake thats different (i to j-1 are same)
        i = j;
    }
    if(str[str.length()-1] == '+') return chunks-1;
    return chunks;
}

int main(){
    ifstream input("B-large.in");
    ofstream output("largeB.txt");
    int t;
    input >> t;
    for(int i=0;i<t;i++){
        string str;
        input >> str;
        cout << "Case #" << i+1 << ": " << solve2(str) << endl;
        output << "Case #" << i+1 << ": " << solve2(str) << endl;
    }
	input.close();
	output.close();
	return 0;
}
