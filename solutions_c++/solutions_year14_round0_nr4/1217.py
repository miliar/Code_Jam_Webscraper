#include <iostream>

using namespace std;

float *kenBlocks, *naomiBlocks;
int numOfBlocks;

void setBlocks(float* blocks);
int playWar();
int playDeceitfulWar();
int kenMove(float naomiChosen);
void burnBlock(float* blocks, int pos);
int findLightestBlock(float* blocks);
int findHeavierBlock(float* blocks);

int main(void){
    int numOfCases, pointsForWar, pointsForDeceitfulWar, i, initialNumOfBlocks;
    cin >> numOfCases;
    for(i=1; i<=numOfCases; i++){
        cin >> initialNumOfBlocks;
        numOfBlocks = initialNumOfBlocks;
        kenBlocks = new float[numOfBlocks];
        naomiBlocks = new float[numOfBlocks];
        setBlocks(naomiBlocks);
        setBlocks(kenBlocks);
        pointsForWar = playWar();
        numOfBlocks = initialNumOfBlocks;
        pointsForDeceitfulWar = playDeceitfulWar();
        cout << "Case #" << i << ": " << pointsForDeceitfulWar << " " << pointsForWar;
        cout << endl;
        delete[] kenBlocks;
        delete[] naomiBlocks;
    }
}

void setBlocks(float* blocks){
    for(int i=0; i<numOfBlocks; i++){
        cin >> blocks[i];
    }
}

int playWar(){
    int naomiPoints, naomiChosen, kenChosen;
    naomiPoints=0;
    while(numOfBlocks!=0){
        naomiChosen = 0;
        kenChosen = kenMove(naomiBlocks[naomiChosen]);
        if(naomiBlocks[naomiChosen]>kenBlocks[kenChosen]){
            naomiPoints++;
        }
        burnBlock(naomiBlocks, naomiChosen);
        burnBlock(kenBlocks, kenChosen);
        numOfBlocks--;
    }
    return naomiPoints;
}

int playDeceitfulWar(){
    int naomiPoints, naomiChosen, possibleKenChosen, kenChosen;
    float toldNaomi;
    naomiPoints=0;
    while(numOfBlocks>1){
        naomiChosen = findLightestBlock(naomiBlocks);
        possibleKenChosen = findLightestBlock(kenBlocks);
        if(naomiBlocks[naomiChosen]>kenBlocks[possibleKenChosen]){
            //Obligates Ken to play his lightest block
            toldNaomi = kenBlocks[findHeavierBlock(kenBlocks)]+0.000001;
        }
        else{
            //Obligates Ken to play his heavier block
            toldNaomi = kenBlocks[findHeavierBlock(kenBlocks)]-0.000001;
        }
        kenChosen = kenMove(toldNaomi);
        if(naomiBlocks[naomiChosen]>kenBlocks[kenChosen]){
            naomiPoints++;
        }
        burnBlock(naomiBlocks, naomiChosen);
        burnBlock(kenBlocks, kenChosen);
        numOfBlocks--;
    }
    naomiPoints+=playWar();
    return naomiPoints;
}

int kenMove(float naomiChosen){
    float lastWeight = 1;
    int block=-1;
    for(int i=0; i<numOfBlocks; i++){
        if(kenBlocks[i]>naomiChosen && kenBlocks[i]<lastWeight){
            block = i;
            lastWeight = kenBlocks[i];
        }
    }
    if(block<0){
        block = findLightestBlock(kenBlocks);
    }
    return block;
}

void burnBlock(float* blocks, int pos){
    int i;
    float temp;
    temp = blocks[pos];
    for(i = pos; i<numOfBlocks-1; i++){
        blocks[i] = blocks[i+1];
    }
    blocks[i] = temp;
}

int findHeavierBlock(float* blocks){
    int i, block;
    block=0;
    for(i=1; i<numOfBlocks; i++){
        if(blocks[i]>blocks[block]){
            block=i;
        }
    }
    return block;
}

int findLightestBlock(float* blocks){
    int i, block;
    block=0;
    for(i=1; i<numOfBlocks; i++){
        if(blocks[i]<blocks[block]){
            block=i;
        }
    }
    return block;
}
