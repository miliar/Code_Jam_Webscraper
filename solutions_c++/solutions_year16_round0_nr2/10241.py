#include<iostream>
#include<fstream>
#include<string>
#include<deque>
#include<stack>
#include<map>
#include<set>

using namespace std;

class Pancakes_Data{
    public:
        string pancakes;
        int level;

        Pancakes_Data(string pancakes, int level){
            this->pancakes = pancakes;
            this->level = level;
        }
};

int main(){

    ofstream myfile;
    myfile.open ("output.in");

    int T;
    cin>>T;

    for(int case_i = 1 ; case_i<=T ; case_i++){

        string input;
        cin>>input;

        deque<Pancakes_Data> pancakes_queue;
        pancakes_queue.push_back(Pancakes_Data(input,0));

        map<int,int> childtoparent;
        set<string> unique_pancakes;

        int minimumsteps = 0;

        while(1){
            Pancakes_Data pancakes_data = pancakes_queue.front();
            pancakes_queue.pop_front();

            string pancakes = pancakes_data.pancakes;
            unique_pancakes.insert(pancakes);

            //cout<<"starting with "<<pancakes<<endl;
            int level = pancakes_data.level;

            bool happypancakefound = true;
            for(int pancake_i=0 ; pancake_i < pancakes.length(); pancake_i++){
                if(pancakes[pancake_i] == '-')
                    happypancakefound = false;
            }

            if(happypancakefound) {
                minimumsteps = level;
                break;
            }

            for(int pancake_i=0 ; pancake_i < pancakes.length(); pancake_i++){

                string newpancakes = "";
                stack<char> pickedpancakes;
                int pickedpancake_i = 0;

                for(; pickedpancake_i <= pancake_i; pickedpancake_i++){
                    pickedpancakes.push(pancakes[pickedpancake_i]);
                }

                while(!pickedpancakes.empty()){
                    char pancake = pickedpancakes.top();
                    pickedpancakes.pop();

                    if(pancake == '+')
                        newpancakes = newpancakes + '-';
                    else
                        newpancakes = newpancakes + '+';
                }

                for(; pickedpancake_i < pancakes.length(); pickedpancake_i++){
                    newpancakes = newpancakes + pancakes[pickedpancake_i];
                }

                //cout<<"newpancakes = "<<newpancakes<<" level = "<<level+1<<endl;

                if(unique_pancakes.count(newpancakes) == 0){
                    Pancakes_Data newpancakes_data(newpancakes,level+1);
                    pancakes_queue.push_back(newpancakes_data);
                }
            }
        }

//        pancakes_queue.clear();
        myfile<<"Case #"<<case_i<<": "<<minimumsteps<<endl;
    }

    return 0;
}
