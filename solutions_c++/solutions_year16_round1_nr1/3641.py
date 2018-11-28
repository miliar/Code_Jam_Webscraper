#include <iostream>
#include <sstream>
#include <string>


using namespace std;

string doCompute(string input);

int main(){
    long t;
    cin >> t;
    long long tc = 1;
    for(long long int i = 0;i< t; i++){
        string s;
        cin >> s;
        s = doCompute(s);
        cout << "Case #" <<  tc++ << ": " << s <<  endl;
    }
    return 0;
}

string doCompute(string input){
    string output = "";
    output += input.at(0);
    for(long long i = 1; i < input.length(); i++){
         if(input.at(i) >= output.at(0)){
            output = input.at(i) + output;
         }
         else/*(input.at(i) <= output.length() - 1)*/{
            output+= input.at(i);
         }
        // cout << "Resultado parcial " << output << endl;
    }
    return output;
}




// #include <iostream>
// #include <sstream>
// #include <string>

// int currentPoint;
// long int totalFlips = 0;
// using namespace std;

// bool checkBegin(string s);
// string getWhatMatters(string input);
// string doMovement(string pancakeStack);
// bool checkHappiness(string pancakeStack);
// int workfor2(string s);
// bool checkPlus(string s);


// int main(){
//     int t;
//     cin >> t;
//     for(long long int i = 0;i< t; i++){
//         string s;
//         cin >> s;
//         if(checkPlus(s)){
//             cout << "Case #" << i+1 << ": 0" << endl;
//         }
//         else if(s.length() == 2){
//             int result = workfor2(s);
//             cout << "Case #" << i+1 << ": " << result << endl;
//         }
//         else {
//             currentPoint = 1;
//             totalFlips = 0;
//           //  cout << s.length() << endl;
//             s = getWhatMatters(s);
//             while(checkHappiness(s) == false){
//                // cout << s << endl;
//                 s = doMovement(s);
//                 //cout  << s << endl;
//             }
//             cout << "Case #" << i+1 << ": " << totalFlips << endl;
//         }
//     }
// }

// int workfor2(string s){
//     if(s == "+-")
//         return 2;
//     else if(s == "-+")
//         return 1;
//     else if(s == "--")
//         return 1;
//     else
//         return 0;
// }


// bool checkBegin(string s){
//     bool minus = false;
//     for(long long int i = 0;i < s.length();i++){
//         if(s.at(i) == '-')
//             minus = true;
//     }
//     if(minus)
//         return true;
//     else
//         return false;
// }

// // - + - - - | + +
// // - - + + - + - - - | + +
// // + + + + - + - - - | + +
// // - - - - - + - - - | + +
// // + + + + + + - - - | + +
// // - - - - - - - - - | + +
// // + + + + + + + + + | + +

// string getWhatMatters(string input){
//     string output = "";
//     long long int newPancakeStack;
//     for(long long int i = input.length() - 1; i >=0; i--){
//         if(input.at(i) == '-'){
//             newPancakeStack = i;
//             break;
//         }
//     }
//     for(long long int i = 0; i <= newPancakeStack; i++){
//         output += input.at(i);
//     }
//     return output;
// }

// string doMovement(string pancakeStack){
//     string aux= "";
//     string rev = "";
//     long long int position_to_turn;
//     char initial = pancakeStack.at(0);
//     bool foundUnequal = false;
//     for(long long int i = currentPoint; i < pancakeStack.length(); i++){
//         if(pancakeStack.at(i) != initial){
//             position_to_turn = i;
//             currentPoint = i;
//             foundUnequal = true;
//             break;

//         }
//     }
//     if(!foundUnequal){
//         totalFlips++;
//         return "+";
//     }
//     for(long long int i = position_to_turn-1; i >= 0; i--){
//         if(pancakeStack.at(i) == '-')
//             aux += "+";
//         else
//             aux += "-";
//     }
//     for(long long int i = 0;i< position_to_turn; i++){
//         pancakeStack.at(i) = aux.at(i);
//     }
//     totalFlips++;
//     return pancakeStack;
// }

// bool checkHappiness(string pancakeStack){
//     for(long long int i = 0;i < pancakeStack.length(); i++ ){
//         if(pancakeStack.at(i) == '-')
//             return false;
//     }
//     return true;
// }

// bool checkPlus(string s){
//     for(int i = 0; i < s.length(); i++){
//         if(s.at(i) == '-')
//             return false;

//     }
//     return true;
// }





// // #include <iostream>
// // #include <sstream>
// // #include <string>

// // using namespace std;

// //     bool x0=false;
// //     bool x1=false;
// //     bool x2=false;
// //     bool x3=false;
// //     bool x4=false;
// //     bool x5=false;
// //     bool x6=false;
// //     bool x7=false;
// //     bool x8=false;
// //     bool x9=false;
// //     string value;

// // bool check();

// // int doTheMath(string value);
// // void reset();

// // int main(){
// //     long long int t;
// //     long long int n;
// //     cin >> t;
// //     for(long long int i = 0;i < t; i++){
// //         cin >> n;
// //         if(n == 0)
// //             cout << "CASE #" << i+1 <<": INSOMNIA" << endl;
// //         else {
// //             long long int index = 1;
// //             reset();
// //             string value;
// //          //   cout << "Here!" << endl;
// //             long long int n_copy = n;
// //             while(check() == false){
// //                 value = to_string(n_copy);
// // //cout << "Value: " << value << endl;
// //                 doTheMath(value);
// //                 n_copy = ++index * n;
// //             }
// //             cout << "CASE #" << i+1 <<": " << value << endl;
// //         }
// //     }
// // }




// // bool check(){
// //     if(x0 &&  x1 && x2 && x3 && x4 && x5 && x6 && x7 && x8 && x9)
// //         return true;
// //     else
// //         return false;
// // }

// // int doTheMath(string value){
// //     for(int i = 0; i < value.length(); i++){
// //         if(value.at(i) == '0')
// //             x0 = true;
// //         else if(value.at(i) == '1')
// //             x1 = true;
// //         else if(value.at(i) == '2')
// //             x2 = true;
// //         else if(value.at(i) == '3')
// //             x3 = true;
// //         else if(value.at(i) == '4')
// //             x4 = true;
// //         else if(value.at(i) == '5')
// //             x5 = true;
// //         else if(value.at(i) == '6')
// //             x6 = true;
// //         else if(value.at(i) == '7')
// //             x7 = true;
// //         else if(value.at(i) == '8')
// //             x8 = true;
// //         else
// //             x9 = true;
// //     }
// //     return 0;
// // }

// // void reset(){
// //     x0=false;
// //     x1=false;
// //     x2=false;
// //     x3=false;
// //     x4=false;
// //     x5=false;
// //     x6=false;
// //     x7=false;
// //     x8=false;
// //     x9=false;
// // }
