#include <iostream>
#include <iomanip>

using namespace std;

int input();
int process();
int printResult();

int count;
long double c, f, x;
long double result;

int main ( void ){
    int i;
    int count;

    cin >> count;

    for( i = 0; i < count; i++ ){
        input();
        process();
        cout << "Case #" << i + 1 << ": ";
        printResult();
    }

    return 0;
}

int input(){
    cin >> c >> f >> x;
    //cout << "C: " << c << endl;
    //cout << "F: " << f << endl;
    //cout << "X: " << x << endl;

    return 0;
}

int process(){
    long double wait;
    long double farm;
    long double production = 2;
    result = 0;

    while( true ){
        wait = x / production;
        farm = ( c / production ) + ( x / ( production + f ) );

        //cout << "Production: " << production << endl;
        //cout << "Wait: " << wait << endl;
        //cout << "Farm: " << farm << endl;
        //cout << "Result: " << result << endl;

        if( wait <= farm ) break;
        result += c / production;
        production += f;
    }

    result += wait;

    return 0;
}

int printResult(){
    int i;

    cout << fixed << setprecision( 7 );
    cout << result << endl;
    
    return 0;
}
