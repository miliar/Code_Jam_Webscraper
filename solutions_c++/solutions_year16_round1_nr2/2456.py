//
//  main.cpp
//  Rank and File
//
//  Created by Rugen Heidbuchel on 16/04/16.
//  Copyright © 2016 Rugen Heidbuchel. All rights reserved.
//

#include <iostream>
#include <vector>
#include <queue>
#include <set>

struct PartialField {
    std::set<size_t> doneRows;
    std::set<size_t> doneColumns;
    std::vector<std::vector<size_t>> field;
};


size_t T, N;

bool isCorrectField(PartialField &partialField) {
    
    size_t last;
    for (size_t r = 0; r < N; r++) {
        last = partialField.field[r][0];
        for (size_t c = 1; c < N; c++) {
            if (partialField.field[r][c] > 0) {
                if (partialField.field[r][c] <= last) {
                    return false;
                }
                last = partialField.field[r][c];
            }
        }
    }
    for (size_t c = 0; c < N; c++) {
        last = partialField.field[0][c];
        for (size_t r = 1; r < N; r++) {
            if (partialField.field[r][c] > 0) {
                if (partialField.field[r][c] <= last) {
                    return false;
                }
                last = partialField.field[r][c];
            }
        }
    }
    
    return true;
}

int main(int argc, const char * argv[]) {
    
    #ifdef USE_INPUT_FILE
    freopen("input.txt", "r", stdin);
    #endif
    
    // MAIN Begin
    
    std::cin >> T;
    for (size_t caseNumber = 0; caseNumber < T; caseNumber++) {
        
        std::cout << "Case #" << caseNumber + 1 << ":";
        
        std::cin >> N;
        
        std::queue<PartialField> queue;
        bool found = false;
        
        PartialField beginField = PartialField();
        beginField.field = std::vector<std::vector<size_t>>(N, std::vector<size_t>(N));
        
        queue.push(beginField);
        
        std::vector<size_t> rank(N);
        
        while (!queue.empty() && !found) {
            
            for (size_t i = 0; i < N; i++) {
                std::cin >> rank[i];
            }
            
            size_t todo = queue.size();
            for (size_t i = 0; i < todo; i++) {
                
                PartialField partialField = queue.front(); queue.pop();
                
                for (size_t r = 0; r < N; r++) {
                    
                    if (partialField.doneRows.find(r) != partialField.doneRows.end()) {
                        continue;
                    }
                    
                    bool possible = true;
                    for (size_t c = 0; c < N; c++) {
                        if (partialField.field[r][c] != 0 && partialField.field[r][c] != rank[c]) {
                            possible = false;
                            break;
                        }
                    }
                    
                    if (possible) {
                        PartialField partialFieldCopy = partialField;
                        for (size_t c = 0; c < N; c++) {
                            partialFieldCopy.field[r][c] = rank[c];
                        }
                        if (isCorrectField(partialFieldCopy)) {
                            partialFieldCopy.doneRows.insert(r);
                            if (2*N - partialFieldCopy.doneRows.size() - partialFieldCopy.doneColumns.size() == 1) {
                                
                                if (partialFieldCopy.doneRows.size() == N) {
                                    for (size_t c = 0; c < N; c++) {
                                        if (partialFieldCopy.doneColumns.find(c) == partialFieldCopy.doneColumns.end()) {
                                            for (size_t row = 0; row < N; row++) {
                                                std::cout << " " << partialFieldCopy.field[row][c];
                                            }
                                            break;
                                        }
                                    }
                                } else {
                                    for (size_t row = 0; row < N; row++) {
                                        if (partialFieldCopy.doneRows.find(row) == partialFieldCopy.doneRows.end()) {
                                            for (size_t c = 0; c < N; c++) {
                                                std::cout << " " << partialFieldCopy.field[row][c];
                                            }
                                            break;
                                        }
                                    }
                                }
                                found = true;
                                break;
                            }
                            queue.push(partialFieldCopy);
                        }
                    }
                }
                
                if (found) {
                    break;
                }
                
                for (size_t c = 0; c < N; c++) {
                    
                    if (partialField.doneColumns.find(c) != partialField.doneColumns.end()) {
                        continue;
                    }
                    
                    bool possible = true;
                    for (size_t r = 0; r < N; r++) {
                        if (partialField.field[r][c] != 0 && partialField.field[r][c] != rank[r]) {
                            possible = false;
                            break;
                        }
                    }
                    
                    if (possible) {
                        PartialField partialFieldCopy = partialField;
                        for (size_t r = 0; r < N; r++) {
                            partialFieldCopy.field[r][c] = rank[r];
                        }
                        if (isCorrectField(partialFieldCopy)) {
                            partialFieldCopy.doneColumns.insert(c);
                            if (2*N - partialFieldCopy.doneRows.size() - partialFieldCopy.doneColumns.size() == 1) {
                                
                                if (partialFieldCopy.doneRows.size() == N) {
                                    for (size_t c = 0; c < N; c++) {
                                        if (partialFieldCopy.doneColumns.find(c) == partialFieldCopy.doneColumns.end()) {
                                            for (size_t row = 0; row < N; row++) {
                                                std::cout << " " << partialFieldCopy.field[row][c];
                                            }
                                            break;
                                        }
                                    }
                                } else {
                                    for (size_t row = 0; row < N; row++) {
                                        if (partialFieldCopy.doneRows.find(row) == partialFieldCopy.doneRows.end()) {
                                            for (size_t c = 0; c < N; c++) {
                                                std::cout << " " << partialFieldCopy.field[row][c];
                                            }
                                            break;
                                        }
                                    }
                                }
                                found = true;
                                break;
                            }
                            queue.push(partialFieldCopy);
                        }
                    }
                }
                
                if (found) {
                    break;
                }
            }
        }
        
        std::cout << std::endl;
    }
    
    // MAIN End
    
    return 0;
}