#include <iostream>
#include <string>
#include <vector>
#include <string>
#include <limits.h>
#include <fstream>
#include <unordered_map>
using namespace std;

string mult_table[8][8] = {
                            {"1", "i", "j", "k","-1", "-i", "-j", "-k"}, 
                            {"i","-1","k","-j","-i","1","-k","j"},
                            {"j","-k","-1","i","-j","k","1","-i"},
                            {"k","j","-i","-1","-k","-j","i","1"},
                            {"-1", "-i", "-j", "-k","1", "i", "j", "k"}, 
                            {"-i","1","-k","j","i","-1","k","-j"},
                            {"-j","k","1","-i","j","-k","-1","i"},
                            {"-k","-j","i","1","k","j","-i","-1"}
                          };

string multiplyhelper(string first, string second) {
    unordered_map<string, int> map_index;
    map_index["1"] = 0;
    map_index["i"] = 1;
    map_index["j"] = 2;
    map_index["k"] = 3;
    map_index["-1"] = 4;
    map_index["-i"] = 5;
    map_index["-j"] = 6;
    map_index["-k"] = 7;
    //cout<< first <<"   "<<second<<endl;
    return mult_table[map_index[first]][map_index[second]];
}

string divi(string result, string first) {
    unordered_map<string, int> map_index;
    map_index["1"] = 0;
    map_index["i"] = 1;
    map_index["j"] = 2;
    map_index["k"] = 3;
    map_index["-1"] = 4;
    map_index["-i"] = 5;
    map_index["-j"] = 6;
    map_index["-k"] = 7;

    vector<string> str_vec;
    str_vec.push_back("1");
    str_vec.push_back("i");
    str_vec.push_back("j");
    str_vec.push_back("k");
    str_vec.push_back("-1");
    str_vec.push_back("-i");
    str_vec.push_back("-j");
    str_vec.push_back("-k");


    for(int i = 0; i < 8; ++i) {
        if(mult_table[map_index[first]][i] == result)
            return str_vec[i];
    }
    return "";
}

// string multiply(string first, char second) {
//     string result = "";
//     if(first.length() == 2)  result += "-";
//     string new_result = multiplyhelper(first[first.length()-1], second);
//     if(new_result.length() == 2) {
//         if(result.length()>0) result = new_result.substr(1,1);
//         else
//             result += new_result;
//     }
//     else
//         result += new_result;
//     return result;
// }


// string multi(vector<char>& whole_vec, int st, int ed, vector< vector<string> >& mem_res) {
//     if(mem_res[st][ed]!="") return mem_res[st][ed];

//     // mem_res[st][ed] = multiply(mem_res[st][ed-1], whole_vec[ed]);
//     // return mem_res[st][ed];
//     string cur = "" + string(1,whole_vec[st]);
//     for(int i = st+1; i <= ed; ++i) {
//         cur = multiply(cur,whole_vec[i]);
//     }
//     mem_res[st][ed] = cur;
//     return cur;
// }


int main() {
    ifstream fin("C-small-attempt0.in");
    ofstream fout("3_out.txt");
    int testNum, l ,x;
    fin >> testNum;
    vector<char> chr_vec;
    vector<char> whole_vec;
    char tmp_chr;
    // unordered_map<string, int> map_index;
    // map_index["1"] = 0;
    // map_index["i"] = 1;
    // map_index["j"] = 2;
    // map_index["k"] = 3;
    // map_index["-1"] = 5;
    // map_index["-i"] = 6;
    // map_index["-j"] = 7;
    // map_index["-k"] = 8;
    for(int i = 1; i <= testNum; ++i) {

        fin >> l >> x;

        for(int j = 1; j <= l ;++j){
            fin>>tmp_chr;
            chr_vec.push_back(tmp_chr);
        }
        for(int k = 1; k <= x; ++k) {
            whole_vec.insert(whole_vec.end(), chr_vec.begin(), chr_vec.end());
        }

        bool find_flag = false;
        // vector< vector<string> > mem_res;
        // vector<string> mem_row;
        // for(int i = 0; i< whole_vec.size(); ++i) {
        //         mem_row.push_back("");
        // }
        // for(int j = 0; j< whole_vec.size(); ++j) {
        //     mem_res.push_back(mem_row);
        //     //cout<<j<<endl;
        // }   

        //get muti_vec
        vector<string> multi_vec;
        vector<int> feas_i;
        string cur_result = string(1,whole_vec[0]);
        multi_vec.push_back(cur_result);
        if(cur_result == "i") feas_i.push_back(0);
        for(int i = 1; i < whole_vec.size(); ++i) {
            
            cur_result = multiplyhelper(cur_result, string(1,whole_vec[i]));
            if((cur_result == "i")&&(i < int(whole_vec.size())-3))
                feas_i.push_back(i);
            multi_vec.push_back(cur_result);
        }

        //feas_j
        vector<int> feas_j;
        cout<<i<<endl;
        for(int index_1 = 0; index_1 < feas_i.size(); ++index_1){
           
            if(index_1 == 0){
                for(int index_2 = index_1 + 1; index_2 <= int(whole_vec.size())-2; ++index_2){
                        string j_to_end = divi(multi_vec[multi_vec.size()-1], multi_vec[index_2]);
                        if(j_to_end != "k") continue;
                        else
                            feas_j.push_back(index_2);
                        string i_to_j = divi(multi_vec[index_2], multi_vec[feas_i[index_1]]);
                        if( i_to_j != "j") continue;
                        find_flag = true;
                        break;
                }
            }   
            else {
                for(int index_2 = 0; index_2 < feas_j.size(); ++index_2) {
                    if(feas_j[index_2] > feas_i[index_1]){
                        string i_to_j = divi(multi_vec[feas_j[index_2]], multi_vec[feas_i[index_1]]);
                        if(i_to_j != "j") continue;
                        find_flag = true;
                        break;
                    }
                }
            }

            if(find_flag) 
                break;
        }

        // cout<<feas_i.size()<<endl;
        // for(int index_1 = 0; index_1 < feas_i.size(); ++index_1){
            
        //     cout<<index_1<<endl;
        //     if(multi_vec[feas_i[index_1]] != "i") continue;
        //     for(int index_2 = index_1 + 1; index_2 <= int(whole_vec.size())-2; ++index_2){

        //         string i_to_j = divi(multi_vec[index_2], multi_vec[feas_i[index_1]]);
        //         if( i_to_j != "j") continue;
        //         string j_to_end = divi(multi_vec[multi_vec.size()-1], multi_vec[index_2]);
        //         if(j_to_end != "k") continue;
        //         find_flag = true;
        //         break;

        //     }
        //     if(find_flag) 
        //         break;
        // }

        // for(int index_1 = 0; index_1 <= int(whole_vec.size())-3; ++index_1){
        //     if(multi(whole_vec,0,index_1,mem_res) != "i") continue;
        //     for(int index_2 = index_1 + 1; index_2 <= int(whole_vec.size())-2; ++index_2){
        //         if((multi(whole_vec, index_1+1, index_2,mem_res) == "j") &&(multi(whole_vec, index_2+1, whole_vec.size()-1,mem_res)=="k")){
        //             find_flag = true;
        //             break;
        //         }
        //         cout<<index_1<<" "<<index_2<<endl;
        //     }
        //     if(find_flag) break;

        // }
        
        if(find_flag) fout<<"Case #"<<i<<": "<<"YES"<<endl;
        else fout<<"Case #"<<i<<": "<<"NO"<<endl;

        chr_vec.clear();
        whole_vec.clear();

    }
    return 0;
}



// int getMin(vector<int>& vec) {
//     int min = INT_MAX;
//     for(int i = 0; i< vec.size(); ++i) {
//         if(vec[i] < min) 
//             min = vec[i];
//     }
//     return min;
// }

// int getMax(vector<int>& vec) {
//     int max = INT_MIN;
//     for(int i = 0; i< vec.size(); ++i) {
//         if(vec[i] > max) 
//             max = vec[i];
//     }
//     return max;
// }
// vector<int> setMaxHalf(vector<int> vec) {
//     int max = INT_MIN;
//     int max_index = 0;
//     for(int i = 0; i< vec.size(); ++i) {
//         if(vec[i] > max){ 
//             max = vec[i];
//             max_index = i;
//         }
//     }
//     vec[max_index] = max/2;
//     vec.push_back(max-max/2);
//     return vec;
// }
// vector<int> minusOne(vector<int> vec) {
//     for(int i =0; i < vec.size(); ++i) {
//         if(vec[i] > 0)
//             vec[i] -= 1;
//     }
//     return vec;
// }

// void GetPlateNum(vector<int>& plate_vec, int step_need, int& cur_min) {
//     //end condition
//     if(getMax(plate_vec) == 2){
//         step_need += 2;
//         if(cur_min > step_need) {
//             cur_min = step_need;
//         }
//         return;
//     }
//     if(getMax(plate_vec) == 1){
//         step_need += 1;
//         if(cur_min > step_need) {
//             cur_min = step_need;
//         }
//         return;
//     }
//     //two possibility
//     //give to others, get max, set to 1
//     vector<int> maxHalf = setMaxHalf(plate_vec);
//     GetPlateNum(maxHalf, step_need + 1, cur_min);
    
//     //eat for the minute
//     vector<int> minuOne = minusOne(plate_vec);
//     GetPlateNum(minuOne, step_need+1, cur_min);
// }
// int main()
// {
//   ifstream fin("B-small-attempt0.in");
//   ofstream fout("out-B-small.txt");
//   int testNum;
//   fin >> testNum;
//   vector<int> plate_vec;
//   for (int i = 1; i<= testNum; ++i) {
//     int non_emp;
//     int temp_plt;
//     fin >> non_emp;
//     for (int j = 1; j <= non_emp; ++j) {
//         fin >> temp_plt;
//         plate_vec.push_back(temp_plt);
//     }
//     //plate_vec
//     int step_need = 0;
//     int cur_min = INT_MAX;
//     GetPlateNum(plate_vec, step_need, cur_min);
//     fout << "Case #" << i<<": "<<cur_min <<endl;
//     plate_vec.clear();
//   }

// }
