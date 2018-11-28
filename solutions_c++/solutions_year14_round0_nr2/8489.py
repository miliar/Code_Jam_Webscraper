#include "../input/gcj-input.h"
#include <vector>
#include <stdlib.h>
#include <iostream>

using namespace std;

class cookie_game
{
public:
    double farm_cost;
    double farm_rate;
    double goal;
    double cookies;
    double current_rate;
    double current_time;
    bool done = false;

    double time_to_next_decision(){
        return (farm_cost - cookies) / current_rate; 
    }
    double eta(){
        return (goal - cookies) / current_rate;
    }
    double eta_after_buying(){
        return (goal - cookies + farm_cost) / (current_rate + farm_rate);
    }
    void advance(double t_diff){
        cookies += current_rate * t_diff;
        current_time += t_diff;
    }
    void buy(){
        cookies -= farm_cost;
        current_rate += farm_rate;
    }
    
};

int main(int argc, char const *argv[])
{
    const string filename = argv[1];
    GcjInput in(filename);
    int T = in.read_line_of_ints(1).at(0);

    for (int i = 1; i<=T; i++){
        vector<double> values = in.read_line_of_doubles(3);
        cookie_game game;
        game.farm_cost = values[0];
        game.farm_rate = values[1];
        game.goal = values[2];
        game.cookies = 0.0;
        game.current_rate = 2.0;
        game.current_time = 0;
        cout.precision(7);

        while(!game.done){

            if(game.eta() > game.time_to_next_decision())
            {
                //cout << "TIME/COOKIES BEFORE ADVANCING" << game.current_time << ' ' << game.cookies << endl;
                game.advance(game.time_to_next_decision());

                if(game.eta() > game.eta_after_buying()){
                    game.buy();
                }
                else{
                    game.advance(game.eta());
                    cout << fixed << "Case #" << i <<": " << game.current_time << endl;
                    game.done = true;
                    continue;
               }
            }
            else
            {
                game.advance(game.eta());
                cout << fixed << "Case #" << i <<": " << game.current_time << endl;
                game.done = true;
                continue;
            }

        }
    }

    return 0;
}
